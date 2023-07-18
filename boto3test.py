import boto3

AWS_ACCESS_KEY = "test"
AWS_SECRET_ACCESS_KEY = "test"
AWS_DEFAULT_REGIN = "ap-northeast-2"

def main():
    session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_DEFAULT_REGIN)

    s3 = session.resource('s3')

    for bucket in s3.buckets.all():
        print(bucket.name)


if __name__ == '__main__':
    main()