# kokkai-mcp
国会会議録のMCPサーバ構築実験。


## 開発環境構築

1. `DevContainers`を起動
2. [MinIO](http://localhost:9001/access-keys)にアクセスして、アクセスキー発行
3. `.env.example`を参考に、`.env.local`を作成する。
4. `make init-bucket`を実行する。
