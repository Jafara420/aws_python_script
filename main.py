import argparse
from s3.crud import list_buckets, create_bucket, delete_bucket
from s3.magic import upload_file_by_type

# This script provides a command-line interface for managing AWS S3 buckets and files.

def main():
    parser = argparse.ArgumentParser(
        description="AWS Service Management CLI Tool",
        epilog="Use 'python main.py <command> --help' to get help on a specific command."
    )

    subparsers = parser.add_subparsers(
        dest="command",
        title="Available Commands",
        description="These are the supported AWS operations"
    )
    
    # List Buckets command
    subparsers.add_parser(
        "list-buckets",
        help="List all S3 buckets in your AWS account"
    )

    # Create Bucket command
    create_parser = subparsers.add_parser(
        "create-bucket",
        help="Create a new S3 bucket, input bucket name with --name tag"
    )
    create_parser.add_argument(
        "--name", required=True, help="The name of the new bucket"
    )

    # Delete Bucket command
    delete_parser = subparsers.add_parser(
        "delete-bucket",
        help="Delete an S3 bucket, input bucket name with --name tag"
    )
    delete_parser.add_argument(
        "--name", required=True, help="The name of the bucket to delete"
    )

    # Upload file in bucket command
    upload_parser = subparsers.add_parser(
        "upload-file",
        help="Upload a file to an S3 bucket, input bucket name with --bucket and file path with --file"
    )
    upload_parser.add_argument(
        "--bucket-name", required=True, help="The name of the bucket to upload to"
    )
    upload_parser.add_argument(
        "--file", required=True, help="The path to the file to upload"
    )
   


    args = parser.parse_args()

    if args.command == "list-buckets":
        bucket_list = list_buckets()
        if bucket_list:
            print("S3 Buckets:")
            print(f"Found {len(bucket_list)} buckets on current AWS account:")
            for bucket in bucket_list:
                print(f"  {bucket}")
        else:
            print("No buckets found.")
    
    elif args.command == "create-bucket":
        if not args.name:
            print("Bucket name is required.")
            exit(1)
        response = create_bucket(args.name)
        if response:
            print(f"Bucket {args.name} created successfully.")
        else:
            print(f"Failed to create bucket {args.name}.")

    elif args.command == "delete-bucket":
        if not args.name:
            print("Bucket name is required.")
            exit(1)
        response = delete_bucket(args.name)

    elif args.command == "upload-file":
        if not args.bucket_name or not args.file:
            print("Bucket name and file path are required.")
            exit(1)
        response = upload_file_by_type(args.bucket_name, args.file)
        if response:
            print(f"File {args.file} uploaded to bucket {args.bucket_name} successfully.")
    else:
        parser.print_help()
        exit(1)



if __name__ == "__main__":
    main()
