include .env.local

upload:
	MINIO_ACCESS_KEY=${MINIO_ACCESS_KEY} MINIO_SECRET_KEY=${MINIO_SECRET_KEY} \
	uv run python -m src.cmd.upload

init-bucket:
	@echo "Creating bucket on MinIO"
	export AWS_ACCESS_KEY_ID=${MINIO_ACCESS_KEY} && export AWS_SECRET_ACCESS_KEY=${MINIO_SECRET_KEY} && \
	aws s3api create-bucket --bucket ${BUCKET_NAME} \
		--endpoint-url ${MINIO_ENDPOINT} --region ap-northeast-1 && \
	POLICY='{"Version":"2012-10-17","Statement":[{"Sid":"PublicReadGetObject","Effect":"Allow","Principal":"*","Action":"s3:GetObject","Resource":"arn:aws:s3:::${BUCKET_NAME}/*"}]}' && \
	aws s3api put-bucket-policy --bucket ${BUCKET_NAME} --policy $$POLICY \
		--endpoint-url ${MINIO_ENDPOINT} --region ap-northeast-1
.PHONY: init-bucket

mcp:
	S3URI="http://localhost:9000/kokkai-mcp-bucket/kokkai_speech_2025-01-01_2025-04-30.parquet" \
	uv run python -m src.cmd.mcp


gen-client:
	kiota generate -l python -d "https://yyyoichi.github.io/kokkai-api-schema/schema/openapi.yaml" -n client -o ./src/kokkaiapiclient