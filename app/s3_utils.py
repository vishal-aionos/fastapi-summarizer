# app/s3_utils.py
import boto3
import os
import requests
from uuid import uuid4
from dotenv import load_dotenv
from botocore.exceptions import BotoCoreError, NoCredentialsError

# Load environment variables
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET = os.getenv("AWS_S3_BUCKET")

# Create S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

def download_and_upload_pdf(url, company_name: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        file_id = str(uuid4())
        # Folder + file structure
        filename = f"{company_name.lower().replace(' ', '_')}/{file_id}.pdf"

        # Upload to S3
        s3.put_object(Bucket=BUCKET, Key=filename, Body=response.content)

        s3_uri = f"s3://{BUCKET}/{filename}"
        return s3_uri

    except (requests.RequestException, BotoCoreError, NoCredentialsError) as e:
        print(f"Error in download/upload: {e}")
        return None
