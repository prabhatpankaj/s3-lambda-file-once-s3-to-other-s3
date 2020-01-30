import boto3
import os
import sys

s3_resource = boto3.resource('s3')
distt_bucket = 'lambdatest0102'
def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        copy_source = {
            'Bucket': bucket,
            'Key': key
        }
        s3_resource.meta.client.copy(copy_source, distt_bucket,key)
        s3_resource.Object(bucket, key).delete()
    return "process completed"
