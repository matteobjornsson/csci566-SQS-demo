# csci566-SQS-demo

## If you haven't already, connect your VirtualBox to the internet. 


Get your wireless interface
```bash
ifconfig
```
Mine is `wlp3s0`

Connect your virtualbox to your wireless interface. Click the settings cog on your virtualbox manager.

![settings](img/virtualbox.png)

Enable your Network Adapter 1 and attach it to the `Bridged Adapter`. Select the name which corresponds to the network interface you want to use from your local machine, such as your wireless interface you discovered using `ifconfig`.

![network](img/networkSettings.png)

Bonus, if you want to enable copy-paste and haven't already, do that in the General > Advanced tab. 

![copy-paste](img/copyPaste.png)

# Set up SQS demo repo

```bash
git clone https://github.com/matteobjornsson/csci566-sqs-demo

pip install boto3
```

```bash
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

```bash
cd ~
mkdir .aws
vim credentials
```
The `~/.aws/credentials` file should look like the file below:
```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```
Additionally, you will want to configure your 

