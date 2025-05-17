from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from dataclasses import dataclass
import os
from typing import Callable

from mcp.server.fastmcp import FastMCP
from src.duckdb import DuckDB
from src.sentence_transformers import encode_text

s3uri = os.getenv("S3URI")

@dataclass
class AppContext:
    # 発言内容をベクトル化する関数
    embedding: Callable[[list[str]], list[list[float]]]
    db: DuckDB


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Manage application lifecycle with type-safe context"""
    # Initialize on startup
    if s3uri is None:
        raise ValueError("S3URI environment variable is not set")
    db = DuckDB(s3uri=s3uri)
    try:
        yield AppContext(db=db, embedding=encode_text)
    finally:
        db.con.close()


mcp = FastMCP("国会会議録検索サーバ", 
              dependencies=["duckdb", "sentence_transformers"],
              lifespan=app_lifespan,
              )


@mcp.resource("kokkai://speech-uris/{prompt}",
              name="国会発言URL検索",
              mime_type="text/plain",
              description="入力されたプロンプトに類似する国会会議録中の発言を検索してそのURLを返します。")
def search_speech_urls(prompt: str) -> str:
    print(f"search_speech_urls: {prompt}")
    ctx: AppContext = mcp.get_context().request_context.lifespan_context # type: ignore
    vec = ctx.embedding([prompt])[0]
    print(f"\tgot: {len(vec)} vectors")
    db = ctx.db
    ids = db.query(vec)
    print(f"\tgot: {len(ids)} ids")
    urls = [f"https://kokkai.ndl.go.jp/api/speech?speechID={id}&recordPacking=json" for id in ids]
    return f"「{prompt}」で類似判定された国会会議録の発言は、関連度順に以下のリンクにアクセスしてください。"+"\n- ".join(urls)