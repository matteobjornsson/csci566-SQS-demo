import boto3
from time import sleep
from datetime import datetime
import aws.message_wrapper as message_wrapper
from botocore.exceptions import ClientError

sqs = boto3.resource('sqs')
queue = sqs.Queue('https://sqs.us-east-1.amazonaws.com/622058021374/csci566_jobs')

job = 0 
while True:
    job += 1

    now = datetime.now()
    timestamp = now.strftime("%m/%d/%Y, %H:%M:%S")

    message = f"Here is a job you should process. Job number {job}.\n"

    message_attributes = {
                'timestamp': {'StringValue': timestamp, 'DataType': 'String'},
                'jobnumber': {'StringValue': str(job), 'DataType': 'String'}
                }

    response = message_wrapper.send_message(queue, message, message_attributes)
    print(f"Job {job} sent.")
    sleep(1)




