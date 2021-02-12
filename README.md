# AWS Simple Queue Service in Python
 
# Hackathon

1. Set up environment and credentials, and run existing `message_wrapper.py` file to test that everything is working. 

1. Write a consumer for a job queue that pulls jobs from the queue below and "processes" them (put some delay between checks for messages and just pull one at a time so everyone can pull messages).
    * The job queue: https://sqs.us-east-1.amazonaws.com/622058021374/csci566_jobs

1. Create your own queue (either programmatically in python or in the online console). Send the queue `arn` as a string to the following SQS url to register your queue with the topic:
    * `https://sqs.us-east-1.amazonaws.com/622058021374/subscribe_to_csci566`

1. Change your policy settings in your personal queue by adding the following JSON to your queue policy within the "Statements" list: 

    ```json
    {
        "Effect": "Allow",
        "Principal": {
          "Service": "sns.amazonaws.com"
        },
        "Action": "sqs:SendMessage",
        "Resource": "arn:aws:sqs:us-east-1:123456789012:YOUR_QUEUE",
        "Condition": {
          "ArnEquals": {
            "aws:SourceArn": "arn:aws:sns:us-east-1:622058021374:csci566_group_messaging"
          }
        }
      }
    ```
    This allows your queue to be sent messages from the topic. You will recieve a "confirmation" message on your personal queue you created. Poll for messages on your queue in your online console to find the "confirm subscripiton" URL. Visit that URL with your browser to confirm your subscription. 

1. Write a client that sends string messages to said topic:
    * `arn:aws:sns:us-east-1:622058021374:csci566_group_messaging`

    If done correctly, all queues registered will recieve your messages. 

1. If we still have time, change the plumbing on the secure comms hackathon to use SQS queues. 

1. [A great podcast](https://podcasts.apple.com/us/podcast/sqs-sns-and-kinesis/id1507582049?i=1000475787493) that is a short and sweet overview of SQS, SNS, and Kinesis. 


# Environment
Basic: (Don't push to this repo)
```bash
$ git clone https://github.com/matteobjornsson/csci566-sqs-demo.git
```
Recommended: 

If you would like to pull updates from my repository but push your updates to your own fork or clone or whatnot, you could also go onto github, fork my repository, download that, then set my repository (not your fork) as an remote named upstream. Ignore this if you don't feel like keeping your work in your hown GitHub repo.  
```bash
$ git clone https://github.com/YOURUSERNAME/csci566-sqs-demo.git
```
```bash
$ git remote -v
> origin  https://github.com/YOURUSERNAME/csci566-sqs-demo.git (fetch)
> origin  https://github.com/YOURUSERNAME/csci566-sqs-demo.git (push)
```
```bash
$ git remote add upstream https://github.com/matteobjornsson/csci566-sqs-demo.git
```
```bash
$ git remote -v
> origin    https://github.com/YOURUSERNAME/csci566-sqs-demo.git (fetch)
> origin    https://github.com/YOURUSERNAME/csci566-sqs-demo.git (push)
> upstream  https://github.com/matteobjornsson/csci566-sqs-demo.git (fetch)
> upstream  https://github.com/matteobjornsson/csci566-sqs-demo.git (push)
```
You would then pull any updates from this repo into yours via
```bash
$ git pull upstream main
```
## Configure AWS Credentials

### If you have an education account, do the following:

(If you need help setting up an account, use [this guide](https://github.com/matteobjornsson/csci566-sqs-demo/blob/main/awsEducate.md))

1. Log into your Vocareum account at https://labs.vocareum.com/
1. Click on the `Account Details` Button.
1. Click on the `Show` Button next to `AWS CLI:`
1. Copy all of the text there. These are your credentials that will be pasted into your credentials file at `~/.aws/credentials`.

### If you have a non-educational account, do the following:

1. Log into your account at https://console.aws.amazon.com/
1. Click on your name top right corner and then `My Security Credentials`.
1. Click `Create New Access Key` and follow instructions. 
1. Create the `~/.aws/credentials` file in your VirtualBox as indicated below but substitute in your real access key and secret key. 

Make sure the `~/.aws` directory exists and create/edit a credentials file there:
```bash
$ cd ~
$ mkdir .aws
$ vim .aws/credentials
```
Copy paste your credentials such that the `~/.aws/credentials` file looks like the text below but with your access key and secret access key:
```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
aws_session_token = YOUR_TOKEN (Only for educate accounts)
```
Additionally, you will want to configure your region:

```bash
$ vim ~/.aws/config
```
Which should look like this: 
```
[default]
region = us-east-1
```
## Install Python Dependencies
This code uses python3, which is installed on the virtual machine. 

```bash
$ pip3 install boto3
```
# Test Out That The Existing Code Works

This should test the basic AWS SQS credential and SDK functionality. A properly functioning environment and credentials will create a queue, send something like 200 messages and recieve them. 

```bash
$ cd /WHEREVER_YOU_PUT_THE_REPO/csci566-sqs-demo/code/aws
$ python3 message_wrapper.py
```
Success looks like this: 
```
> Running the usage demonstration uses your default AWS account credentials and might incur charges on your account. Do you want to continue (y/n)? y
> Starting the usage demo. Enjoy!
> Sending file lines in batches of 10 as messages.
> ............................Done. Sent 277 messages.
> Receiving, handling, and deleting messages in batches of 10.
> ................................Done.
> Successfully reassembled all file lines!
```

Failure looks like this: 
```
> Running the usage demonstration uses your default AWS account credentials and might incur charges on your account. Do you want to continue (y/n)? y
> Starting the usage demo. Enjoy!
> Couldn't create queue named 'sqs-usage-demo-message-wrapper'.
> Traceback (most recent call last):
  File "/home/csci566/Desktop/csci566-sqs-demo/code/queue_wrapper.py", line 61, in create_queue
    queue = sqs.create_queue(
  File "/home/csci566/.local/lib/python3.8/site-packages/boto3/resources/factory.py", line 520, in do_action
    response = action(self, *args, **kwargs)
  File "/home/csci566/.local/lib/python3.8/site-packages/boto3/resources/action.py", line 83, in __call__
    response = getattr(parent.meta.client, operation_name)(*args, **params)
  File "/home/csci566/.local/lib/python3.8/site-packages/botocore/client.py", line 357, in _api_call
    return self._make_api_call(operation_name, kwargs)
  File "/home/csci566/.local/lib/python3.8/site-packages/botocore/client.py", line 676, in _make_api_call
    raise error_class(parsed_response, operation_name)
botocore.exceptions.ClientError: An error occurred (SignatureDoesNotMatch) when calling the CreateQueue operation: The request signature we calculated does not match the signature you provided. Check your AWS Secret Access Key and signing method. Consult the service documentation for details.

... etc
```
note from amazon: 

>Amazon SQS Free Tier*
>
>You can get started with Amazon SQS for free. All customers can make 1 million Amazon SQS requests for free each month. 
# Extra Links and Docs

* General intro via Amazon docs

    * https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html

* The Python SDK documentation for SQS

    * https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html

* The python example code provided by Amazon:

    * https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code/sqs
    * The test suite has some dependencies in the higher level directories, which have been copied to `test/test_tools`.

* For those interested in a stripped down HTTP version of using SQS, check out this article:
    * https://blog.iron.io/amazon-sqs-simple-queue-service-overview-and-tutorial/


