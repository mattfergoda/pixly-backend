import os
from dotenv import load_dotenv
import boto3
from botocore.exceptions import ClientError
import logging

load_dotenv()

AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
REGION = os.environ['REGION']
BUCKET_NAME = os.environ['BUCKET_NAME']


s3 = boto3.client(
  "s3",
  REGION,
  aws_access_key_id=AWS_ACCESS_KEY,
  aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def upload_file(image_binary, file_name, content_type='image/jpeg'):
    """Upload a file to an S3 bucket

    :param image_binary: Image binary file to upload
    :param file_name: file_name. Will correspond to object key in S3
    :return: aws_image_src: URL to image in S3
     """

    # Upload the file
    try:
        # response = s3.upload_file(file_name, bucket, object_name)
        s3.put_object(
            Body=image_binary,
            Bucket=BUCKET_NAME,
            Key=file_name,
            ContentType=content_type
        )

        # url = f"{bucket_name}.s3.{location}.amazonaws.com/{key}"
        aws_image_src = f'{BUCKET_NAME}.s3.{REGION}.amazonaws.com/{file_name}'

    except ClientError as e:
        logging.error(e)
        return

    return aws_image_src


def get_s3_file(file_name):
    """ Takes in a file name , returns StreamingBody object """

    response = s3.get_object(Bucket=BUCKET_NAME, Key=file_name)
    return response["Body"]