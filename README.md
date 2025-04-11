
# 🛠️ AWS Service Management CLI Tool

A powerful Python-based command-line tool to manage **AWS S3 buckets** with ease. Create, list, delete buckets, and upload files—all from your terminal.  
Built with `boto3` for seamless AWS integration.

```
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

```

---

## ✨ Features

- 📦 **List Buckets** – See all your S3 buckets.
- 🪣 **Create Bucket** – Instantly spin up a new bucket.
- 🗑️ **Delete Bucket** – Remove unwanted S3 buckets.
- ☁️ **Upload File** – Upload files intelligently based on file type.

More AWS services will be integrated soon, including Lambda, EC2, and more!

---

## 🚀 Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/aws-cli-tool.git
    cd aws-cli-tool
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

---

## ⚙️ Usage

This tool allows you to interact with **AWS S3** via the command line.

### Available Commands

- **`list-buckets`**: List all S3 buckets in your AWS account
- **`create-bucket`**: Create a new S3 bucket  
  Use `--name` to specify the bucket name.
- **`delete-bucket`**: Delete an S3 bucket  
  Use `--name` to specify the bucket name.
- **`upload-file`**: Upload a file to a specific S3 bucket  
  Use `--bucket-name` to specify the bucket and `--file` to provide the file path.

---

### Command Examples

#### List S3 Buckets

```bash
python main.py list-buckets
```

#### Create a New S3 Bucket

```bash
python main.py create-bucket --name your-bucket-name
```

#### Delete an S3 Bucket

```bash
python main.py delete-bucket --name your-bucket-name
```

#### Upload a File to a Bucket

```bash
python main.py upload-file --bucket-name your-bucket-name --file path/to/your/file.txt
```

---

## 🛠️ Prerequisites

Before using this tool, ensure you have the following:

- Python 3.x
- An AWS account with **S3** access
- AWS Access Key ID and Secret Access Key
- **Required Python packages**: `boto3`, `python-dotenv`

---

## 🔒 Required Environment Variables

You need to configure your AWS credentials and region in a `.env` file at the root of your project:

```env
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_REGION=us-east-1  # The AWS region for S3 bucket creation
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.