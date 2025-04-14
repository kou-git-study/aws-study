import boto3
import base64

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    bucket = 'my-api-bucket-202504'  # ←バケット名をここに！
    key = event['queryStringParameters']['file']  # sample.rtf など
    
    try:
        s3_object = s3.get_object(Bucket=bucket, Key=key)
        file_data = s3_object['Body'].read()

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/rtf",
                "Content-Disposition": f"attachment; filename={key}"
            },
            "isBase64Encoded": True,
            "body": base64.b64encode(file_data).decode('utf-8')
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
