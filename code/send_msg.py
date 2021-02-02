
import boto3
import message_wrapper as mw

sqs = boto3.resource('sqs')
q_csci566 = sqs.Queue('https://sqs.us-east-1.amazonaws.com/622058021374/csci566')

response = mw.send_message(queue=q_csci566, message_body='test message')

print("Message " + response['MessageId'] + " sent.\n")

messages = mw.receive_messages(q_csci566, 5, 20)

for msg in messages:
    print("Message " + msg.message_id + " received: ")
    print("Body: " + msg.body, '\n', "Attributes: " + str(msg.message_attributes))

mw.delete_messages(q_csci566, messages)