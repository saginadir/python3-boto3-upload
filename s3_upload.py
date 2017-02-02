import os
import sys

import boto3


def upload_to_s3(bucket, key, file_path, callback=None, md5=None, reduced_redundancy=False, content_type=None):

    s3 = boto3.resource('s3')

    data = open(file_path, 'rb')

    try:
        s3.Bucket(bucket).put_object(Key=key, Body=data)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

    return True
