import boto3
import os
import time

class S3Handler:
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    aws_region = os.environ.get('AWS_REGION')
    bucket_name = os.environ.get('AWS_BUCKET_NAME')

    def get_file_list(self):
        s3 = boto3.resource("s3", aws_access_key_id=self.aws_access_key_id,
                                 aws_secret_access_key=self.aws_secret_access_key,
                                  region_name=self.aws_region)
        bucket = s3.Bucket(self.bucket_name)
        exts = ['.xlsx', '.xls', '.xlt', '.xltx']
        file_list = []
        for bucket_object in bucket.objects.all():
            key = bucket_object.key
            for ext in exts:
                if key.endswith(ext):
                    file_list.append({
                        'key': bucket_object.key,
                        'last_modified': bucket_object.last_modified
                    })
                    continue
        return file_list

    def upload_file(self, file_path, file_name):
        s3_client = boto3.client('s3', aws_access_key_id=self.aws_access_key_id,
                                 aws_secret_access_key=self.aws_secret_access_key, region_name=self.aws_region)
        s3_client.upload_file(file_path, self.bucket_name, file_name)

    def download_file(self, key):
        s3_client = boto3.client('s3', aws_access_key_id=self.aws_access_key_id,
                                 aws_secret_access_key=self.aws_secret_access_key, region_name=self.aws_region)
        download_path = "%s%s" % (time.time(), os.path.splitext(key)[1])
        s3_client.download_file(self.bucket_name, key, download_path)
        return download_path
