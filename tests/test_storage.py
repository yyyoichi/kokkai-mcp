
import os
from contextlib import contextmanager
from mypy_boto3_s3 import S3Client
from botocore.exceptions import ClientError
from src.storage import StorageClient, get_minio_client

def load_env():
    # load /workspace/.env.local
    assert os.path.exists("/workspaces/.env.local")
    with open("/workspaces/.env.local") as f:
        for line in f:
            key, value = line.strip().split("=")
            os.environ[key] = value

@contextmanager
def storage_client_manager(bucket_name: str):
    load_env()
    endpint_url = os.getenv("MINIO_ENDPOINT")
    access_key = os.getenv("MINIO_ACCESS_KEY")
    secret_key = os.getenv("MINIO_SECRET_KEY")
    assert endpint_url is not None
    assert access_key is not None
    assert secret_key is not None

    client: S3Client = get_minio_client(
        endpoint_url=endpint_url,
        access_key=access_key,
        secret_key=secret_key,
    )


    client.create_bucket(Bucket=bucket_name)

    storage_client_instance = StorageClient(client=client, bucket_name=bucket_name)

    try:
        yield storage_client_instance
    finally:
         # delete all objects in the bucket
        objects = client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in objects:
            for obj in objects['Contents']:
                if 'Key' not in obj:
                    continue
                client.delete_object(Bucket=bucket_name, Key=obj['Key'])
        # delete the bucket
        client.delete_bucket(Bucket=bucket_name)



def test_storage():

    ## emptyを確認するヘルパーテスト
    def test_empty_storage(client: StorageClient):
        try:
            client.download_parquet(2023, 1)
        except ClientError as e:
            err = e.response.get("Error", None)
            if err is not None:
                assert err.get("Code") == "NoSuchKey"
            else:
                assert False, "Expected a ClientError with NoSuchKey"
            ...
        else:
            assert False, "Expected an exception to be raised"

    with storage_client_manager("test-storage-bucket") as client:
        # download
        test_empty_storage(client)
        # upload
        import io
        buffer = io.BytesIO(b"test")
        client.upload_parquet(2023, 1, buffer)
        # download
        buffer = client.download_parquet(2023, 1)
        assert buffer.getvalue() == b"test"
        # remove
        client.remove_parquet(2023, 1)
        # download
        test_empty_storage(client)




