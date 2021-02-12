import boto3
from aws.sns_basics import SnsWrapper

sns = boto3.resource('sns')
sns_wrapper = SnsWrapper(sns)
topic = sns.Topic('arn:aws:sns:us-east-1:622058021374:csci566')

while True:
    message = input("\nEnter a message to send to the topic 'csci566': \n")
    response = sns_wrapper.publish_message(topic=topic, message=message, attributes={})
    print(f"Message {response} published to topic")
