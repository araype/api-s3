import boto3
import json  # ← agregar esto

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = json.loads(event['body'])['bucket'] 
    
    # Proceso    
    s3 = boto3.client('s3')
    response = s3.list_objects(Bucket=nombre_bucket)
    lista = []
    for obj in response['Contents']:
        lista.append(obj['Key'])

    return {
        'statusCode': 200,
        'bucket': nombre_bucket,
        'lista_objetos': lista
    }