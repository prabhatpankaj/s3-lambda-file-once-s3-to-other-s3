import boto3
import os
import sys
from datetime import datetime

s3_resource = boto3.resource('s3')
distt_bucket = 'lambdatest0102'
def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        currenttime = datetime.utcnow()
        timeformat = currenttime.strftime("%d-%m-%Y-%H-%M-%S")
        filepath, filename = os.path.split(key)
        newfilename = timeformat + '-' + filename
        newkey = os.path.join(filepath, newfilename)
        copy_source = {
            'Bucket': bucket,
            'Key': key
        }
        s3_resource.meta.client.copy(copy_source, distt_bucket, newkey)
        s3_resource.Object(bucket, key).delete()
    return "process completed"
