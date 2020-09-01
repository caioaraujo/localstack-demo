# Demo de uso da lib localstack
import boto3

import json


def main():

    # Acesso ao S3
    s3 = boto3.resource('s3', endpoint_url="http://localhost:4572")
    bucket_demo = s3.Bucket("bucket-demo")

    for s3_object in bucket_demo.objects.filter(Prefix="minha-pasta-logs/log"):
        log = json.loads(s3_object)


if __name__ == '__main__':
    main()
