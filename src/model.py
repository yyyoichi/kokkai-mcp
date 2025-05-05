from dataclasses import dataclass

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
