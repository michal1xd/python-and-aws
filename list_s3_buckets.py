import boto3

s3_client = boto3.client('s3')

response = s3_client.list_buckets()

print("S3 Buckets in your account:")
for bucket in response['Buckets']:
    bucket_name = bucket["Name"]
    creation_date = bucket['CreationDate']
    print(f" -> Found bucket '{bucket_name}' created on {creation_date.strftime('%Y-%m-%d')}")