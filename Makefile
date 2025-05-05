include .env.local

init-bucket:
	@echo "Creating bucket on MinIO"
	export AWS_ACCESS_KEY_ID=${MINIO_ACCESS_KEY} && export AWS_SECRET_ACCESS_KEY=${MINIO_SECRET_KEY} && \
	aws s3api create-bucket --bucket ${BUCKET_NAME} \
		--endpoint-url ${MINIO_ENDPOINT} --region ap-northeast-1 && \
	POLICY='{"Version":"2012-10-17","Statement":[{"Sid":"PublicReadGetObject","Effect":"Allow","Principal":"*","Action":"s3:GetObject","Resource":"arn:aws:s3:::${BUCKET_NAME}/*"}]}' && \
	aws s3api put-bucket-policy --bucket ${BUCKET_NAME} --policy $$POLICY \
		--endpoint-url ${MINIO_ENDPOINT} --region ap-northeast-1
.PHONY: init-bucket