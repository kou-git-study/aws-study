
# AWS構成：API Gateway to S3 ＆ SOAP通信風EC2

## 概要

このリポジトリは、AWSの **API Gateway → S3連携** と、**SOAP通信風のEC2構成** を実装したプロジェクトです。

- AWSサービスの選定（API Gateway,Lambda,S3, EC2,IAM など）
- ネットワーク設計（セキュリティグループ、ルートテーブル、NACL）
- アクセス検証（curl による通信テスト）
**基本設計～詳細設計レベル**まで、自身で構成・構築・動作確認まで一貫して行いました。

今後、Lambdaを入れた構成やTerraformなどのIaC化を入れて、さらに設計力を高めていく予定です。

---

## 使用AWSサービス

- VPC / サブネット / ルートテーブル / NACL / IGW
- EC2（FlaskによるSOAP風エンドポイント）
- API Gateway（HTTP API）
- Lambda（S3からファイルを取し、バイナリで返却）
- S3（GETオブジェクト用）
- IAM（API GatewayからS3アクセス用のロール）

---

## ディレクトリ構成

```
.
api-gateway-soap-develop/
├── README.md
├── apigw-to-s3/
│   ├── lambda/
│   │   └── download_file.py
│   ├── terraform/
│   │   └── apigateway_s3.tf（これから追加予定）
│   └── screenshots/
│       └── test_result.png（curlテストなど）
└── soap-communication/
    └── （これから追加予定）
---

## 🔗 curlテスト例

S3用（API Gateway経由）
curl https://<your-api-id>.execute-api.<region>.amazonaws.com/default/sample.txt

SOAP用（EC2のIPを指定）
curl -X POST http://<EC2-Public-IP>/soap \
-H "Content-Type: text/xml" \
-d '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
      <soapenv:Body>
        <test>Hello</test>
      </soapenv:Body>
    </soapenv:Envelope>'

---

## ポイント

- AWSのコンソールを使って自ら構築・検証
- ネットワーク構成（SG、NACL、ルートテーブル）に意図を持って設計
- API Gateway → S3構成ではIAMロールやメソッド設定を理解
- シンプルな構成だが「設計→構築→テスト」の一連を体験済み

