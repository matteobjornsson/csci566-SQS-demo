import boto3
import aws.message_wrapper as message_wrapper
from botocore.exceptions import ClientError

sqs = boto3.resource('sqs')
queue = sqs.Queue('https://sqs.us-east-1.amazonaws.com/622058021374/subscribe_to_csci566')

message = input("\nSubmit queue arn to register to the topic:\n")

response = message_wrapper.send_message(queue, message)




