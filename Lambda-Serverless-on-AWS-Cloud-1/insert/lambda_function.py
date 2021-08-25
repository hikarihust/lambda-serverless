import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table    = dynamodb.Table('hocsinh')
    res = table.put_item(
        Item={
            'mahocsinh': '0001',
            'tenhocsinh': 'Vu Dinh Quang'
        }
    )

    return {
        'statusCode': 200,
        'res': res
    }