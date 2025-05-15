

from datetime import date
import io
import pandas as pd
import pytest
import pandas as pd
import pyarrow.parquet as pq
from src.config import SpeechRequestParam, UploadSpeechParquetDependency
from src.kokkaiapiclient.api.speech.speech_get_response import SpeechGetResponse
from src.kokkaiapiclient.models.name_of_house import NameOfHouse
from src.kokkaiapiclient.models.speech_record import SpeechRecord
from src.kokkaiapiclient.models.speech_record_speaker import SpeechRecord_speaker
from src.kokkaiapiclient.models.speech_response import SpeechResponse
from src.model import SpeechParquetModel
from src.task import UploadSpeechParquetTask


@pytest.mark.parametrize(
    "rec_count, expected_rows",
    [
        (1, 1),
        (5, 5),
        (10, 10),
    ],
)
@pytest.mark.asyncio
async def test_upload_parquet_task_table(rec_count: int, expected_rows: int):
    class ApiClientMock:
        def __init__(self, rec_count: int):
            self.rec_count = rec_count

        async def iter_speech(self, p: SpeechRequestParam):
            for i in range(self.rec_count):
                rec = SpeechRecord(
                    date="2024-01-01",
                    session=210,
                    name_of_house=NameOfHouse.衆議院,
                    name_of_meeting="本会議",
                    issue=f"第{i+1}号",
                    issue_i_d="ISSUE_001",
                    speaker=SpeechRecord_speaker("山田だろう"),
                    speech_order=2,
                    speech_i_d="SPEECH_002",
                    speech="発言内容"
                )
                yield SpeechGetResponse(
                    speech_response=SpeechResponse(
                        speech_record=[rec],
                        number_of_return=1,
                    ),
                )

    class StorageClientMock:
        def __init__(self):
            self.uploaded_data: pd.DataFrame = pd.DataFrame()

        def upload_parquet(self, p: SpeechRequestParam, buffer: io.BytesIO) -> None:
            table = pq.read_table(buffer) # type: ignore
            read_df = table.to_pandas() # type: ignore
            self.uploaded_data = read_df

    storage_client = StorageClientMock()
    deps = UploadSpeechParquetDependency(
        api_client=ApiClientMock(rec_count),
        embedding=lambda x: [[0.1, 0.2, 0.3] for _ in x],
        storage_client=storage_client,
    )

    task = UploadSpeechParquetTask(deps)


    await task.run(p = SpeechRequestParam(
        from_date=date.fromisoformat("2023-01-01"),
        until_date=date.fromisoformat("2023-01-02"),
    ))

    # ストレージに読まれた行数をテスト
    assert storage_client.uploaded_data.shape[0] == expected_rows
    

@pytest.mark.parametrize(
    "input, expected",
    [
        (SpeechRecord(
            date="2024-01-01",
            session=210,
            name_of_house=NameOfHouse.衆議院,
            name_of_meeting="本会議",
            issue="第1号",
            issue_i_d="ISSUE_001",
            speaker=SpeechRecord_speaker("山田だろう"),
            speech_order=2,
            speech_i_d="SPEECH_002",
            speech="発言内容"
        ), SpeechParquetModel(
            date="2024-01-01",
            session=210,
            name_of_house=NameOfHouse.衆議院,
            name_of_meeting="本会議",
            issue=1,
            issue_id="ISSUE_001",
            speaker="山田だろう",
            speech_order=2,
            speech_id="SPEECH_002",
            speech_vector=[],
        )),
        (SpeechRecord(
            date="2024-01-01",
            session=210,
            name_of_house=NameOfHouse.衆議院,
            name_of_meeting="本会議",
            issue="第100号",
            issue_i_d="ISSUE_001",
            speaker=SpeechRecord_speaker("山田だろう"),
            speech_order=2,
            speech_i_d="SPEECH_002",
            speech="発言内容"
        ), SpeechParquetModel(
            date="2024-01-01",
            session=210,
            name_of_house=NameOfHouse.衆議院,
            name_of_meeting="本会議",
            issue=100,
            issue_id="ISSUE_001",
            speaker="山田だろう",
            speech_order=2,
            speech_id="SPEECH_002",
            speech_vector=[],
        )),
    ],
)
def test_upload_parquet_task_map_speech_rec_to_model(input: SpeechRecord, expected: SpeechParquetModel):
    """
    SpeechRecordをSpeechParquetModelに変換するテスト
    """
    got = UploadSpeechParquetTask.map_speech_rec_to_model(input)
    assert got.as_dict() == expected.as_dict()
