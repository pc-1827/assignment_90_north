import boto3
import base64

s3 = boto3.client('s3')
BUCKET_NAME = 'my-document-storage-bucket'  # Replace with your bucket name

def lambda_handler(event, context):
    try:
        file_content = event.get('fileContent')  # Base64 encoded string
        file_name = event.get('fileName')        # e.g., 'document.pdf'

        if not file_content or not file_name:
            return {
                'statusCode': 400,
                'body': 'Both fileContent and fileName are required.'
            }

        decoded_bytes = base64.b64decode(file_content)
        s3.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=decoded_bytes)

        return {
            'statusCode': 200,
            'body': f'File {file_name} uploaded successfully.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
