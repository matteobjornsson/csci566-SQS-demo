import boto3
from botocore.exceptions import ClientError

# Write a consumer that pulls messages ("jobs") from the queue named 'csci566'. 
# "Process" them by posting their job ID to a queue of your making on your AWS account

# the boto3 library is used to create objects which model the aws resource
# documetation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#service-resource
sqs = boto3.resource('sqs')
# Here we use the resource to make a queue object from an existing queue URL.
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Queue
queue = sqs.Queue('https://sqs.us-east-1.amazonaws.com/622058021374/csci566')

