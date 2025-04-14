from flask import Flask, request, Response
from zeep import Client
from lxml import etree

app = Flask(__name__)

# サンプルSOAPレスポンスを送るエンドポイント
@app.route('/soap', methods=['POST'])
def soap_service():
    # リクエストのXMLデータを取得
    xml_data = request.data
    
    # ここでは単純にリクエストをそのまま返す処理をする例
    # 必要に応じてSOAPクライアントで処理
    client = Client('http://example.com/soap?wsdl')  # WSDLを指定
    response = client.service.some_method()  # WSDLに基づいてメソッドを呼び出す
    
    # レスポンスをSOAP XML形式で返す
    response_xml = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:web="http://www.example.org/webservice">
       <soapenv:Header/>
       <soapenv:Body>
          <web:response>Hello from Flask SOAP Service</web:response>
       </soapenv:Body>
    </soapenv:Envelope>"""
    
    return Response(response_xml, content_type='text/xml; charset=utf-8')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
