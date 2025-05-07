
import os
from src.client import Client
from src.config import KokkkaiAPIRequestConfig, UploadSpeechParquetDependency
from src.sentence_transformers import encode_text, initialize_model
from src.storage import StorageClient, get_minio_client
from src.task import UploadSpeechParquetTask


async def main(yyyyMM: str):
    endpoint_url = os.getenv("MINIO_ENDPOINT")
    access_key = os.getenv("MINIO_ACCESS_KEY")
    secret_key = os.getenv("MINIO_SECRET_KEY")
    bucket_name = os.getenv("BUCKET_NAME")
    if endpoint_url is None or access_key is None or secret_key is None or bucket_name is None:
        print(f"MINIO_ENDPOINT: {endpoint_url}")
        print(f"MINIO_ACCESS_KEY: {access_key}")
        print(f"MINIO_SECRET_KEY: {secret_key}")
        print(f"BUCKET_NAME: {bucket_name}")
        raise ValueError("MINIO_ENDPOINT, MINIO_ACCESS_KEY, and MINIO_SECRET_KEY, BUCKET_NAME must be set")

    if len(yyyyMM) != 6:
        raise ValueError("yyyyMM must be in the format YYYYMM")
    
    year = int(yyyyMM[:4])
    month = int(yyyyMM[4:6])
    if month < 1 or month > 12:
        raise ValueError("Year must be 2024 or later, and month must be between 1 and 12")
    
    deps = UploadSpeechParquetDependency(
        api_client=Client(config=KokkkaiAPIRequestConfig(refer_cache=True)),
        embedding=encode_text,
        storage_client=StorageClient(
            client=get_minio_client(
                endpoint_url=endpoint_url,
                access_key=access_key,
                secret_key=secret_key,
            ),
            bucket_name=bucket_name,
        ),
    )

    print(f"\nStarting process\nInitializing model...")
    initialize_model()
    print(f"Uploading data for {year}-{month:02}...")
    task = UploadSpeechParquetTask(deps=deps)
    await task.run(
        year=year,
        month=month,
    )



if __name__ == "__main__":
    import asyncio
    import sys
    if len(sys.argv) != 2:
        print("Usage: python -m src.cmd.upload <yyyyMM>")
        sys.exit(1)
    yyyyMM = sys.argv[1]
    try:
        asyncio.run(main(yyyyMM))
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
    print("Upload completed successfully.")