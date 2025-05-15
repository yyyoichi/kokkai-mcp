from dataclasses import dataclass
import datetime
import io
from typing import AsyncGenerator, Callable, Protocol

from src.kokkaiapiclient.api.speech.speech_get_response import SpeechGetResponse


# 党首リスト
# https://www.soumu.go.jp/main_content/000717993.pdf
@dataclass
class PartyLeader:
    party: str
    leader: str

party_leader_list = [
    PartyLeader(party="公明党", leader="石井啓一"),
    PartyLeader(party="国民民主党", leader="玉木雄一郎"),
    PartyLeader(party="参政党", leader="神谷宗幣"),
    PartyLeader(party="社会民主党", leader="福島瑞穂"),
    PartyLeader(party="自由民主党本部", leader="石破茂"),
    PartyLeader(party="日本維新の会", leader="馬場伸幸"),
    PartyLeader(party="日本保守党", leader="百田尚樹"),
    PartyLeader(party="日本共産党中央委員会", leader="田村智子"),
    PartyLeader(party="みんなでつくる党", leader="大津綾香"),
    PartyLeader(party="立憲民主党", leader="野田佳彦"),
    PartyLeader(party="れいわ新選組", leader="山本太郎"),
]

@dataclass
class KokkkaiAPIRequestConfig:
    # キャッシュを参照するかどうか
    refer_cache: bool = False
    # キャッシュ機構を利用するかどうか
    use_cache: bool = True
    # APIの取得間隔
    interval_milsec: int = 1000

    def regularize(self):
        """
        正規化処理を行う
        - use_cacheがFalseの場合、refer_cacheをFalseにする
        - refer_cacheがTrueの場合、use_cacheをTrueにする
        - interval_milsecが0以下の場合、1000にする
        """

        # キャッシュ機構を利用しない場合、refer_cacheをFalseにする
        if not self.use_cache:
            self.refer_cache = False
        # キャッシュを参照する場合、use_cacheをTrueにする
        if self.refer_cache:
            self.use_cache = True
        # APIの取得間隔が0以下の場合、1000にする
        if self.interval_milsec <= 0:
            self.interval_milsec = 1000
        return self


@dataclass
class SpeechRequestParam:
    """
    APIリクエストのパラメータ
    """
    from_date: datetime.date
    until_date: datetime.date
    speaker: list[str] | None = None


@dataclass
class UploadSpeechParquetDependency:
    class SpeechApiClientProtocol(Protocol):
        def iter_speech(
            self, p: SpeechRequestParam,
        ) -> AsyncGenerator[SpeechGetResponse, None]: ...
    class StorageClientProtocol(Protocol):
        def upload_parquet(self, p: SpeechRequestParam, buffer: io.BytesIO) -> None: ...

    # APIの取得クライアント
    api_client: SpeechApiClientProtocol
    # 発言内容をベクトル化する関数
    embedding: Callable[[list[str]], list[list[float]]]
    # ParquetBufferを保存する関数
    storage_client: StorageClientProtocol
