import tarfile
import boto3
import lzma
from botocore.exceptions import NoCredentialsError
from zipfile import ZipFile

aws_access_key = "AWS Key"
secret_access_key = "AWS Secret Access Key"

zip_file_name = "file_name.tar.xz"
dirName = "Directory of items to compress"


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key,
                      aws_secret_access_key=secret_access_key)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return True


if __name__ == '__main__':
    xz_file = lzma.LZMAFile(zip_file_name, mode='w')

    with tarfile.open(mode='w', fileobj=xz_file) as tar_xz_file:
        tar_xz_file.add(dirName)

    xz_file.close()

    uploaded = upload_to_aws("local_file.tar.xz", "bucket", "s3_file")