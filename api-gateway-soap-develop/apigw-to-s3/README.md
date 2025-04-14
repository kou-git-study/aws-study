# API Gateway → S3連携構成

## 📌 概要

この構成では、API GatewayからLambda関数を呼び出し、S3に保存されたファイルをダウンロードするAPIを構築しています。

## 💡 使用サービス

- AWS API Gateway
- AWS Lambda(Python)
- AWS S3
- AWS IAM

## 📝 手順

1. S3バケットを作成しオブジェクトを格納
2. IAMロール・ポリシーの作成（Lambda用）
3. Lambda関数（`lambda/download_file.py`）を作成
4. API Gatewayを作成（HTTP API、GET）
5. LambdaにAPI Gatewayをトリガーとして設定
6. `curl` コマンドでAPIテスト

## 🧪 curlテスト例

```bash
curl -X GET https://your-api-id.execute-api.ap-northeast-1.amazonaws.com/dev/download
