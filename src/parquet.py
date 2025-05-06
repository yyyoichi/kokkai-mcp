
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from src.model import SpeechParquetModel

class SpeechParquet:
    def __init__(self):
        self.buffer = pa.BufferOutputStream()
        self.writer = pq.ParquetWriter(where=self.buffer,schema=SpeechParquetModel.pyarrow_schema(), compression='zstd')

    def append(self, speeches: list[SpeechParquetModel]):
        """
        Append a list of SpeechParquetModel to the Parquet file.
        """
        table = pa.Table.from_pandas(
            df=pd.DataFrame([s.as_dict() for s in speeches]), 
            schema=SpeechParquetModel.pyarrow_schema())
        self.writer.write_table(table)

    def getvalue(self):
        """
        書き込みを終了してBuffer値を取得する。
        """
        self.writer.close()
        ## getvalueするとbufferがcloseになる（self.writer.writerがcloseする）
        return self.buffer.getvalue()



