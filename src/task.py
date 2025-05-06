

from src.client import Client
from src.config import UploadSpeechParquetDependency
from src.sentence_transformers import encode_text
from src.storage import StorageClient, get_minio_client


def upload_speech_parquet(deps: UploadSpeechParquetDependency):
    pass


if __name__ == "__main__":
    # 依存関係を定義
    c = Client()
    deps = UploadSpeechParquetDependency(
        api_client=c, 
        embedding=encode_text, 
        storage_client=StorageClient(client=get_minio_client("", "", ""), bucket_name=""))
    # S3にアップロードす
    upload_speech_parquet(deps)
    