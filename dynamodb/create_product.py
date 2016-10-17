import boto3


def insert(table_name, url):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    table.put_item(
        Item={
            'url': url,
        }
    )
