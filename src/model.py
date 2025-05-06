from dataclasses import dataclass
import pyarrow as pa

from src.kokkaiapiclient.models.name_of_house import NameOfHouse


@dataclass
class SpeechParquetModel:
    """
    発言データのParquetファイルの情報を保持するクラス
    """
    # 日付
    date: str
    # 国会次回
    session: int
    # 院名
    name_of_house: NameOfHouse
    # 会議名
    name_of_meeting: str
    # 号数
    issue: int
    # 会議録ID
    issue_id: str
    # 発言者名
    speaker: str
    # 発言者順序
    speech_order: int
    # 発言ID
    speech_id: str
    # 発言内容ベクトル
    speech_vector: list[float]

    def as_dict(self) -> dict[str, str | int | list[float]]:
        """
        明示的にdictに変換する
        """
        return {
            "date": self.date,
            "session": self.session,
            "name_of_house": self.name_of_house.title(),
            "name_of_meeting": self.name_of_meeting,
            "issue": self.issue,
            "issue_id": self.issue_id,
            "speaker": self.speaker,
            "speech_order": self.speech_order,
            "speech_id": self.speech_id,
            "speech_vector": self.speech_vector
        }

    @staticmethod
    def pyarrow_schema() -> pa.Schema:
        s = pa.schema(fields=[ # type: ignore 
            pa.field('date', pa.string()), # type: ignore
            pa.field('session', pa.int16()),  # type: ignore
            pa.field('name_of_house', pa.string()), # type: ignore
            pa.field('name_of_meeting', pa.string()), # type: ignore
            pa.field('issue', pa.int16()),  # type: ignore
            pa.field('issue_id', pa.string()), # type: ignore
            pa.field('speaker', pa.string()), # type: ignore
            pa.field('speech_order', pa.int16()),  # type: ignore
            pa.field('speech_id', pa.string()), # type: ignore
            pa.field('speech_vector', pa.list_(pa.float32())) # type: ignore
        ])
        return s
