# TikTok-Rare-Username-Checker
## A simple asynchronous tool that checks if a TikTok username is taken or not

## WORK IN PROGRESS - CAN BE INACCURATE 

## About
It is a proxyless tool  that checks the availablity of TikTok usernames in blazing fast
speed. It checks if the http request status code is not ```200```. If it is, it will automatically assume that the TikTok username is not taken. 

This tool is used for educational purposes only. 

## Picture
![Picture](https://i.ibb.co/Nxv536d/Screenshot-156.png)

## How to use
- Python must be installed

1. If you dont have python installed, download python 3.7.6
and make sure you click on the 'ADD TO PATH' option during
the installation.

2. Type ```pip install aiohttp``` in cmd

3.  Add your usernames you want to check in ```usernames.txt```.

4.  Make sure you are in the same directory as the folder you downloaded it in. Type
```python main.py``` in cmd

5. Once it is done running, available usernames will be saved in ```hits.txt```. 
