
import io
import boto3
from mypy_boto3_s3 import S3Client

from src.config import SpeechRequestParam

def get_minio_client(endpoint_url: str, access_key: str, secret_key: str) -> S3Client:
    client: S3Client = boto3.client( # type: ignore
        service_name='s3', # type: ignore
        endpoint_url=endpoint_url,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name='ap-northeast-1',
    )
    return client # type: ignore

class StorageClient:
    def __init__(self, client: S3Client, bucket_name: str):
        self.client = client
        self.bucket_name = bucket_name
    
    def upload_parquet(self, p: SpeechRequestParam, buffer: io.BytesIO):
        """
        ParquetファイルをS3にアップロードする
        """
        file_name = self.__get_parquet_file_name(p)
        self.client.put_object(
            Body=buffer,
            Bucket=self.bucket_name,
            Key=file_name,
        )
    
    def download_parquet(self, p: SpeechRequestParam) -> io.BytesIO:
        """
        S3からParquetファイルをダウンロードする
        """
        file_name = self.__get_parquet_file_name(p)
        response = self.client.get_object(
            Bucket=self.bucket_name,
            Key=file_name,
        )
        return io.BytesIO(response['Body'].read())

    def remove_parquet(self, p: SpeechRequestParam):
        """
        S3からParquetファイルを削除する
        """
        file_name = self.__get_parquet_file_name(p)
        self.client.delete_object(
            Bucket=self.bucket_name,
            Key=file_name,
        )

    @staticmethod
    def __get_parquet_file_name(p: SpeechRequestParam) -> str:
        """
        Parquetファイル名を取得する
        """
        return f"kokkai_speech_{p.from_date.isoformat()}_{p.until_date.isoformat()}.parquet"

    