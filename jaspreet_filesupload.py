import boto3
import logging
from botocore.exceptions import ClientError
import time

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def upload_files(bucket_name, file_list, region):
    """Upload files to an existing S3 bucket"""
    try:
        # Initialize the S3 client with the specified region
        s3_client = boto3.client('s3', region_name=region)
        start_time = time.time()
        
        for file_name in file_list:
            try:
                logger.info(f"Uploading {file_name} to bucket '{bucket_name}'...")
                # Upload file to S3
                s3_client.upload_file(file_name, bucket_name, file_name)
                logger.info(f"{file_name} uploaded successfully.")
            except ClientError as e:
                logger.error(f"Error occurred while uploading {file_name}: {e}")
            except Exception as e:
                logger.error(f"An unexpected error occurred: {e}")
        
        end_time = time.time()
        logger.info(f"Start Time: {time.ctime(start_time)}")
        logger.info(f"End Time: {time.ctime(end_time)}")

    except ClientError as e:
        logger.error(f"ClientError occurred: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

# Variables
bucket_name = 'contentcen301361099.aws.ai'  # Your bucket name
files_to_upload = ['jaspreet1.txt', 'jaspreet2.txt', 'jaspreet3.txt']  # Files to upload
region = 'us-east-1'  # Replace with your bucket's actual region

# Upload files
upload_files(bucket_name, files_to_upload, region)
