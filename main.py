import os

from s3_upload import upload_to_s3

file_path = 'upload-test.txt'

# When uploading to the root of the bucket, keep the subdirectory blank
subdirectory = 'subdirectory/'

# The file path inside the bucket
key = subdirectory + os.path.basename(file_path)

# Change to the bucket of your desires
bucket = 'sagin-test'

upload_to_s3(bucket, key, file_path)