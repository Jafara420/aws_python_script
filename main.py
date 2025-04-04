import argparse
from s3.buckets import list_buckets, create_bucket, delete_bucket

"""
THIS IS A PYTHON SCRIPT WHICH INTERACTS WITH AWS SERVICES, CURRENTLY S3, LATER ON LAMBDA, EC2 AND SO ON
       .--.
      |o_o |
      |:_/ |
     //   \ \
    (|     | )
   /'\_   _/`\
   \___)=(___/

    A     W   W   SSSSS
   A A    W   W  S
  AAAAA   W W W  SSSSS
 A     A  WW WW      S
A       A W   W  SSSSS


CURRENTLY SUPPORTED AWS SERVICES:
- S3: Simple Storage Service

CURRENT CLI COMMANDS:
- list-buckets: List all S3 buckets in your AWS account
- create-bucket: Create a new S3 bucket, add --name tag to specify the bucket name
- delete-bucket: Delete an S3 bucket, add --name tag to specify the bucket name




"""

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
    else:
        parser.print_help()
        exit(1)

if __name__ == "__main__":
    main()
