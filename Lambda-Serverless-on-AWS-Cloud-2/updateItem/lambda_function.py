import boto3
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table_name = 'hocsinh'
    primary_key = {'mahocsinh': event["mahocsinh"]}
    dynamodb_table    = dynamodb.Table(table_name)
    res = dynamodb_table.update_item(
        Key=primary_key,
        UpdateExpression="set tenhocsinh = :tenhocsinh, tentruong = :tentruong",
        ExpressionAttributeValues={
            ':tenhocsinh':event['tenhocsinh'],
            ':tentruong':event['tentruong']
        }
    )
    
    res = dynamodb_table.get_item(Key=primary_key)
    item=res["Item"]

    return item