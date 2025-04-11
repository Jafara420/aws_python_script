from auth import init_client
import os
import mimetypes
from botocore.exceptions import ClientError
import magic

def upload_file_by_type(bucket_name, file_path):
    """
    Detect file extension/type and upload it to an S3 folder based on its extension.
    """
    s3 = init_client()
    try:
        # Detect the MIME type and extension
        mime_type = magic.from_file(file_path, mime=True)
        
        extension = mimetypes.guess_extension(mime_type)
        
        if not extension:
            extension = os.path.splitext(file_path)[1]
        
        ext_folder = extension.lstrip('.').lower()

        s3_key = f"{ext_folder}/{os.path.basename(file_path)}"
        
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"Uploaded '{file_path}' to 's3://{bucket_name}/{s3_key}'")
        
    except ClientError as e:
        print(f"Error uploading file: {e}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")
