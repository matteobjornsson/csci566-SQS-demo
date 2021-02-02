
import boto3
# from botocore.exceptions import ClientError
from message_wrapper import *

sqs = boto3.resource('sqs')
q_csci566 = sqs.Queue('https://sqs.us-east-1.amazonaws.com/622058021374/csci566')

response = send_message(queue=q_csci566, message_body='test message')

print(response)