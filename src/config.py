

from dataclasses import dataclass
import io
from typing import AsyncGenerator, Callable, Protocol

from src.kokkaiapiclient.api.speech.speech_get_response import SpeechGetResponse


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



# iter_speech メソッドを持つプロトコルを定義
class SpeechApiClientProtocol(Protocol):
    def iter_speech(
        self, year: int, month: int
    ) -> AsyncGenerator[SpeechGetResponse, None]: ...

@dataclass
class UploadSpeechParquetDependency:
    # APIの取得クライアント
    api_client: SpeechApiClientProtocol
    # 発言内容をベクトル化する関数
    embedding: Callable[[list[str]], list[list[float]]]
    # ParquetBufferを保存する関数
    save_parquet: Callable[[int, int, io.BytesIO], None]
