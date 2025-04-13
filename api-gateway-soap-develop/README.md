
# AWS構成：API Gateway to S3 ＆ SOAP通信風EC2

## 概要

このリポジトリは、AWSのAPI GatewayとS3、EC2環境を利用した構成設計および構築の実践プロジェクトです。

- AWSサービスの選定（API Gateway, S3, EC2,IAM など）
- ネットワーク設計（セキュリティグループ、ルートテーブル、NACL）
- アクセス検証（curl による通信テスト）
まで、**基本設計～詳細設計レベルの内容を個人で行いました。**

今後、Lambdaを入れた構成やTerraformなどのIaC化を入れて、さらに設計力を高めていく予定です。

---

## 使用AWSサービス

- VPC / サブネット / ルートテーブル / NACL
- EC2 (FlaskでSOAP通信風のエンドポイント)
- API Gateway (HTTP API)
- S3 (GETオブジェクトアクセス)
- IAM（API Gateway用ロール）

---

## ディレクトリ構成

```
.
├── README.md
├── curl_example.sh
```

---

## curlテストスクリプト例

# S3用（API Gateway経由）
curl https://<your-api-id>.execute-api.<region>.amazonaws.com/default/sample.txt

# SOAP用（EC2のIPを指定）
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

