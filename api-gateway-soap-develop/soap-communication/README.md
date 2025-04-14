# 🧼 SOAP Communication API 

このディレクトリは、EC2 上に構築した Flask SOAP サーバと API Gateway を使った通信の構成・手順をまとめたものです。

---

## 📌 構成概要
使用サービス
AWS VPC：EC2が所属するネットワーク環境を構築
AWS  EC2：Flask アプリをホスト
AWS  API Gateway (HTTP API)：SOAP形式のHTTP POSTリクエストをEC2にルーティング
Flask (Python)：SOAP風のXMLを受け取るサーバアプリ

---

## 📝 手順
1. ネットワーク構築（VPC・EC2）
VPC を作成
パブリックサブネット作成
インターネットゲートウェイ（IGW）を作成し、VPC にアタッチ
ルートテーブルを作成し、0.0.0.0/0 に対して IGW を通すよう設定
サブネットにルートテーブルを関連付け
セキュリティグループ作成（以下を許可）
ポート 22（SSH）
ポート 5000（Flask アプリ確認用）
EC2 インスタンスを作成し、作成した VPC・サブネット・SG を割り当て
EC2 にログインして Python3 / pip3 / Flask をセットアップ

2. Flaskアプリケーション構築
Flask アプリ `soap_server.py` を作成して `/soap` エンドポイントを用意
Flask アプリを起動（`python3 soap_server.py`）

3. API Gateway の作成とEC2連携
HTTP API を作成
エンドポイント /soap を作成し、POST メソッドを有効にする
バックエンドに EC2 の URL（例：http://54.xx.xx.xx:5000/soap）を指定
ステージ名を dev としてデプロイ
curl で疎通確認

## 📸 スクリーンショット・動作確認

`curl` コマンドで SOAP リクエストを送信：

```bash
curl -X POST https://{api-id}.execute-api.ap-northeast-1.amazonaws.com/dev/soap \
-H "Content-Type: text/xml" \
-d '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
      <soapenv:Body>
        <test>Hello</test>
      </soapenv:Body>
    </soapenv:Envelope>'
