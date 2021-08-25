import boto3
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table_name = 'hocsinh'
    primary_key = {'mahocsinh': event["mahocsinh"]}
    dynamodb_table    = dynamodb.Table(table_name)
    
    res = dynamodb_table.delete_item(Key=primary_key)

    return res