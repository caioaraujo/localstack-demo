# Demo de uso da lib localstack
import boto3


def main():

    # Acesso ao S3
    s3 = boto3.resource('s3', endpoint_url="http://localhost:4572")
    bucket_demo = s3.Bucket("bucket-demo")

    bucket_notification = bucket_demo.Notification()

    response = bucket_notification.put(
        NotificationConfiguration={
            'TopicConfigurations': [
                {
                    'TopicArn': 'arn:aws:sns:us-east-1:000000000000:meu-topico',
                    'Events': ['s3:ObjectCreated:Copy'],
                },
            ],
            'QueueConfigurations': [
                {
                    'QueueArn': 'arn:aws:sqs:us-east-1:000000000000:minha-fila',
                    'Events': ['s3:ObjectCreated:Put'],
                },
            ],
        }
    )

    print(response)


if __name__ == '__main__':
    main()
