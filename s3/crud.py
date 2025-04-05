import boto3
from auth import init_client
import os 

def list_buckets():
    """
    List all S3 buckets in the account.
    """
    s3 = init_client()
    response = s3.list_buckets()
    bucket_list = [bucket['Name'] for bucket in response['Buckets']]
    return bucket_list


def create_bucket(bucket_name):
    """
    Create a new S3 bucket.
    """
    s3 = init_client()
    region = os.getenv("aws_region_name")

    if region is None:
        print("Region name is not set in the environment variables.")
        return None
    
    if not bucket_name:
        print("Bucket name is required.")
        return None
    try:

        bucket_list = list_buckets()
        if bucket_name in bucket_list:
            print(f"Bucket {bucket_name} already exists.")
            return None
        response = s3.create_bucket(
            Bucket=bucket_name, CreateBucketConfiguration={
            'LocationConstraint': region
        })
        return response
    except Exception as e:
        print(f"Error creating bucket: {e}")
        return None
    

def delete_bucket(bucket_name):
    """
    Delete an S3 bucket.
    """
    s3 = init_client()
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} deleted successfully.")
    except Exception as e:
        print(f"Error deleting bucket: {e}")