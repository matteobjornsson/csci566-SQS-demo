## If you haven't already, connect your VirtualBox to the internet. 


Get your wireless interface
```bash
ifconfig
```

Connect your virtualbox to your wireless interface. Click the settings cog on your virtualbox manager.

![settings](img/virtualbox.png)

Enable your Network Adapter 1 and attach it to the `Bridged Adapter`. Select the name which corresponds to the network interface you want to use from your local machine, such as your wireless interface you discovered using `ifconfig`.

![network](img/networkSettings.png)

Bonus, if you want to enable copy-paste and haven't already, do that in the General > Advanced tab. 

![copy-paste](img/copyPaste.png)