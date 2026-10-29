
import json
import urllib.parse

def lambda_handler(event, context):
    print("S3 Event Received!")

    for record in event.get("Records", []):
        bucket_name = record["s3"]["bucket"]["name"]
        file_name = urllib.parse.unquote_plus(
            record["s3"]["object"]["key"]
        )

        print(f"Bucket name: {bucket_name}")
        print(f"Uploaded file: {file_name}")

    return {
        "statusCode": 200,
        "body": json.dumps("S3 file upload event processed successfully!")
    }
