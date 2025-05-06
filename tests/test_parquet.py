import io
import pandas as pd
import pyarrow.parquet as pq
from src.kokkaiapiclient.models.name_of_house import NameOfHouse
from src.model import SpeechParquetModel
from src.parquet import SpeechParquet


def test_parquet():
    speeches1 = [
         SpeechParquetModel(date="2024-01-01", session=210, name_of_house=NameOfHouse.参議院, name_of_meeting="予算委員会", issue=1, issue_id="ISSUE_001", speaker="佐藤 花子", speech_order=2, speech_id="SPEECH_002", speech_vector=[0.4, 0.5, 0.6]),
         SpeechParquetModel(date="2024-01-02", session=210, name_of_house=NameOfHouse.衆議院, name_of_meeting="本会議", issue=1, issue_id="ISSUE_002", speaker="鈴木 一郎", speech_order=1, speech_id="SPEECH_003", speech_vector=[0.7, 0.8, 0.9])
    ]
    speeches2 = [
         SpeechParquetModel(date="2024-01-03", session=210, name_of_house=NameOfHouse.衆議院, name_of_meeting="予算委員会", issue=2, issue_id="ISSUE_003", speaker="田中 太郎", speech_order=3, speech_id="SPEECH_004", speech_vector=[0.1, 0.2, 0.3]),
         SpeechParquetModel(date="2024-01-04", session=210, name_of_house=NameOfHouse.参議院, name_of_meeting="本会議", issue=2, issue_id="ISSUE_004", speaker="山田 花子", speech_order=4, speech_id="SPEECH_005", speech_vector=[0.4, 0.5, 0.6])
    ]
    # Parquetファイルに書き込む
    sq = SpeechParquet()
    sq.append(speeches=speeches1)
    sq.append(speeches=speeches2)
    # 読みだしてpandasのDataFrameに変換
    buf = sq.getvalue()
    parquet_file = io.BytesIO(buf)
    table = pq.read_table(parquet_file) # type: ignore
    read_df = table.to_pandas() # type: ignore

    # 期待するDataFrameを作成
    all_speeches = speeches1 + speeches2
    expected_df = pd.DataFrame([s.as_dict() for s in all_speeches])
    # データ型をスキーマに合わせて調整 (特に整数型)
    expected_df['session'] = expected_df['session'].astype('int16')
    expected_df['issue'] = expected_df['issue'].astype('int16')
    expected_df['speech_order'] = expected_df['speech_order'].astype('int16')

    # 比較
    pd.testing.assert_frame_equal(read_df, expected_df)