
from datetime import date, datetime
import os
from src.client import Client
from src.config import KokkkaiAPIRequestConfig, SpeechRequestParam, UploadSpeechParquetDependency
from src.sentence_transformers import encode_text, initialize_model
from src.storage import StorageClient, get_minio_client
from src.task import UploadSpeechParquetTask


async def main():
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

    
    deps = UploadSpeechParquetDependency(
        api_client=Client(config=KokkkaiAPIRequestConfig(use_cache=False)),
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
    print(f"Uploading data for 2025-01-01 ~04-30...")
    task = UploadSpeechParquetTask(deps=deps)
    p = SpeechRequestParam(
        from_date=date.fromisoformat("2025-01-01"),
        until_date=date.fromisoformat("2025-04-30"),
        # speaker=[item.leader for item in party_leader_list],
    )
    print(datetime.now())
    await task.run(p)
    print(datetime.now())



if __name__ == "__main__":
    import asyncio
    import sys
    try:
        asyncio.run(main())
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
    print("Upload completed successfully.")