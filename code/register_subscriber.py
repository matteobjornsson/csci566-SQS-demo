import boto3
import json
import re
import aws.message_wrapper as message_wrapper
from aws.sns_basics import SnsWrapper
from botocore.exceptions import ClientError

sqs = boto3.resource('sqs')
queue = sqs.Queue('https://sqs.us-east-1.amazonaws.com/622058021374/subscribe_to_csci566')

sns = boto3.resource('sns')
sns_wrapper = SnsWrapper(sns)
topic = sns.Topic('arn:aws:sns:us-east-1:622058021374:csci566')

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

def subscribe_queue(topic, protocol, endpoint):
        try:
            subscription = topic.subscribe(
                Protocol=protocol, Endpoint=endpoint, ReturnSubscriptionArn=True)
        except ClientError as error:
            raise error
        else:
            return subscription

def main():
    arn_regex = re.compile('arn:aws:sqs*')
    while True:
        msgs = receive_messages(max_messages=5, wait_time=10)
        if msgs:
            print(msgs)
            for msg in msgs:
                print("\nMessage received.")
                print("ID: " + msg.message_id)
                print("Body: " + msg.body)
                print("Attributes: " + str(msg.message_attributes))
                if arn_regex.match(msg.body):
                    subscription = subscribe_queue(topic, 'sqs', msg.body)
                    print("\nQueue subscribed: ", subscription.arn)
                else:
                    print("\nProvided string is not a valid sqs queue arn.")

            del_response = delete_messages(msgs)
            if 'Successful' in del_response:
                print("\nMessages deleted off of queue.")
            else:
                print("Failed to delete messages from queue.")

if __name__ == "__main__":
    main()