import boto3
from botocore.exceptions import ClientError

Bucket_name = "ml-devops-bucket-8675303"

aws_regoin = "eu-central-1"

s3_client = boto3.client("s3", region_name=aws_regoin)

print(f"Attempting to create bucket: {Bucket_name}")

try:
    s3_client.create_bucket(
        Bucket=Bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': aws_regoin
        }
    )
    print(f" -> Success! Bucket '{Bucket_name}' created.")

except ClientError as e:
    error_code = e.response['Error']['Code']
    print(f" -> Error creating bucket: {error_code}")
except Exception as e:
    print(f" -> An unexpected error occurred: {e}")