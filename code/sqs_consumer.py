import boto3
import json
import aws.message_wrapper as message_wrapper
from botocore.exceptions import ClientError

sqs = boto3.resource('sqs')
queue = sqs.Queue('https://sqs.us-east-1.amazonaws.com/622058021374/csci566')

def receive_messages(max_messages, wait_time):
    try:
        messages = queue.receive_messages(
            MaxNumberOfMessages=max_messages,
            WaitTimeSeconds=wait_time
        )
    except ClientError as error:
        raise error
    else:
        return messages

def delete_messages(messages):
    try:
        entries = [{
            'Id': str(index),
            'ReceiptHandle': msg.receipt_handle
        } for index, msg in enumerate(messages)]
        response = queue.delete_messages(Entries=entries)
    except ClientError:
        print("Couldn't delete messages from queue %s", queue)
    else:
        return response

while True:
    msgs = receive_messages(max_messages=5, wait_time=10)
    if msgs:
        for msg in msgs:
            msg_body = json.loads(msg.body)
            print("\nMessage received.")
            print("ID: " + msg.message_id)
            print("Body: " + msg_body['Message'])
            print("Attributes: " + str(msg.message_attributes))

        del_response = delete_messages(msgs)
        if 'Successful' in del_response:
            print("\nMessages deleted off of queue.")
        else:
            print("Failed to delete messages from queue.")