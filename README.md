# AWS Service Management CLI Tool

This Python CLI tool allows you to manage AWS S3 buckets with basic operations such as listing all buckets and creating new ones. It interacts with AWS services using the `boto3` library and allows you to manage your S3 buckets directly from the command line.

## Features

- **List S3 Buckets**: List all S3 buckets in your AWS account.
- **Create S3 Bucket**: Create a new S3 bucket in your desired AWS region.

## Prerequisites

Before using this tool, ensure you have the following:

- Python 3.x
- AWS account with appropriate permissions (Access to S3)
- AWS Access Key ID and Secret Access Key
- **Python packages**: `boto3`, `python-dotenv`

### Install Dependencies

To install the required Python dependencies, run the following command:

```bash
pip install -r requirements.txt
```
## Required Environment Variables

You need to configure your AWS credentials and the region where you want to create the buckets. To do this, create a `.env` file in the root of your project and add the following variables:

```env
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_REGION=us-east-1  # The AWS region for S3 bucket creation
```

You can create or update these variables in your .env file.

