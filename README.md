### Localstack Demo

Este projeto visa demonstrar o uso simulado do ambiente cloud da AWS localmente com a biblioteca localstack (https://github.com/localstack/localstack).

Fluxo de intregação do SNS, SQS e S3 baseado neste tutorial: https://docs.aws.amazon.com/pt_br/AmazonS3/latest/dev/ways-to-add-notification-config-to-bucket.html

## Instalação
`pip install -r requirements.txt`

Para configurar dados de acesso, execute: `aws configure --profile default`

## Execução
`localstack start`

## Criando tópico SNS
`aws --endpoint-url=http://localhost:4575 sns create-topic --name meu-topico`

## Criando fila no SQS
`aws --endpoint-url=http://localhost:4576 sqs create-queue --queue-name minha-fila`

## Inscreva a fila no tópico
`aws --endpoint-url=http://localhost:4575 sns subscribe --topic-arn "sns arn" --protocol sqs --notification-endpoint "sqs arn"`

## Criando bucket S3
`aws --endpoint-url=http://localhost:4572 s3 mb s3://bucket-demo/minha-pasta-logs`

Copiando os arquivos da pasta logs para o bucket:

`aws --endpoint-url=http://localhost:4572 s3 cp logs s3://bucket-demo/minha-pasta-logs --recursive`

Listando os logs no S3:

`aws --endpoint-url=http://localhost:4572 s3 ls s3://bucket-demo/minha-pasta-logs --recursive`

Adicionando a política no S3:

`aws --endpoint-url=http://localhost:4572 s3api put-bucket-policy --bucket bucket-demo --policy file://s3policy.json`