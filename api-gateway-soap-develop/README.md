
# AWS構成：API Gateway to S3 ＆ SOAP通信風EC2

## 概要

このプロジェクトは、以下の2つの構成をAWSマネジメントコンソールを使って構築する手順とテスト方法をまとめたものです。

1. **API Gateway 経由で S3 にアクセスする構成**
2. **Direct Connect + VPC 経由で EC2 上の SOAP 通信風サーバーにアクセスする構成**

---

## 使用AWSサービス

- VPC / サブネット / ルートテーブル / NACL
- EC2 (FlaskでSOAP通信風のエンドポイント)
- API Gateway (REST API)
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

```bash
curl -X POST http://<EC2-Public-IP>/soap -H "Content-Type: text/xml" -d '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
      <soapenv:Body>
        <test>Hello from On-prem</test>
      </soapenv:Body>
    </soapenv:Envelope>'
```

---

## ポイント

- AWSのコンソールを使って自ら構築・検証
- ネットワーク構成（SG、NACL、ルートテーブル）に意図を持って設計
- API Gateway → S3構成ではIAMロールやメソッド設定を理解
- シンプルな構成だが「設計→構築→テスト」の一連を体験済み

