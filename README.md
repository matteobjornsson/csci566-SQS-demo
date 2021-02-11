# AWS Simple Queue Service in Python
 
# Hackathon

1. Set up, test, and run existing python code.
2. ...
3. Profit??


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
## Configure AWS Credentials

### If you have an education account, do the following:

(If you need help setting up an account, use [this guide](https://github.com/matteobjornsson/csci566-sqs-demo/blob/main/awsEducate.md)

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
This assumes you are working on the Virtual machine which defaults `python` and `pip` to python3.8. You should use `python3` or `pip3` if trying this out outside the VM. 
```bash
$ pip install boto3 pytest
```
# Test Out That The Existing Code Works

This should test the basic AWS SQS credential and SDK functionality. 

```bash
$ cd ~/WHEREVER_YOU_PUT_THE_REPO/csci566-sqs-demo/code
$ python -m pytest -o log_cli=1 --log-cli-level=INFO test/test_message_wrapper.py
```
"The '-o log_cli=1 --log-cli-level=INFO' flags configure pytest to output logs to stdout during the test run. Without them, pytest captures logs and prints them only when the test fails." (quoted from [this file](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/python/example_code/sqs/test/test_message_wrapper.py))
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


