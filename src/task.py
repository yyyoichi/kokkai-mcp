import io
from src.config import UploadSpeechParquetDependency
from src.kokkaiapiclient.models.speech_record import SpeechRecord
from src.model import SpeechParquetModel
from src.parquet import SpeechParquet



class UploadSpeechParquetTask:
    def __init__(self, deps: UploadSpeechParquetDependency):
        self.deps = deps

    async def run(self, year: int, month: int) -> None:
        """
        ひと月分の発言をAPIから取得して、Parquet形式で保存する関数
        """
        parquet_buffer = SpeechParquet()
        async for res in self.deps.api_client.iter_speech(year, month):
            if res.speech_response is None or res.speech_response.speech_record is None:
                # 発言がない場合はスキップ
                continue
            models: list[SpeechParquetModel] = [] # len == res.speech_record.len
            sentences: list[str] = [] # len == res.speech_record.len
            for speech in res.speech_response.speech_record:
                m = self.map_speech_rec_to_model(speech)
                models.append(m)
                sentences.append(speech.speech or "")
            # 発言内容をベクトル化する
            embedding = self.deps.embedding(sentences)
            for i, vec in enumerate(embedding):
                models[i].speech_vector = vec
            # Parquetファイルに追加する
            parquet_buffer.append(models)
        # Parquetを出力
        buf = parquet_buffer.getvalue()
        # Parquetを保存する
        self.deps.storage_client.upload_parquet(year, month, io.BytesIO(buf))

    @staticmethod
    def map_speech_rec_to_model(speech: SpeechRecord) -> SpeechParquetModel:
        """
        APIのレスポンスをSpeechParquetModelに変換する
        """
        # 第x号 '第'と'号'を除去して、intに変換
        issue = int((speech.issue or "").replace("第", "").replace("号", "")) if speech.issue else 0
        m = SpeechParquetModel(
            date=speech.date or "",
            session=speech.session or 0,
            name_of_house=speech.name_of_house or "", # type: ignore
            name_of_meeting=speech.name_of_meeting or "",
            issue=issue,
            issue_id=speech.issue_i_d or "",
            speaker=speech.speaker.string if speech.speaker and speech.speaker.string else "",
            speech_order=speech.speech_order or 0,
            speech_id=speech.speech_i_d or "",
            speech_vector=[],
        )
        return m