# ベースイメージ: Python 3.13 (Debian Bullseye ベースの RC 版、または正式リリース版)
# pyproject.toml の requires-python = ">=3.13" に合わせます。
# 正式な 3.13-slim-bullseye が利用可能であればそちらを使用してください。
FROM python:3.13-slim-bullseye AS base

# システムの依存関係と uv のインストール
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    libgfortran5 && \
    pip install --no-cache-dir uv && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml uv.lock ./

# uv を使用して仮想環境を作成し、依存関係をインストール
RUN uv venv && \
    . .venv/bin/activate && \
    uv sync --frozen --extra docker

COPY src ./src

ENTRYPOINT [".venv/bin/python", "-m", "src.cmd.mcp"]