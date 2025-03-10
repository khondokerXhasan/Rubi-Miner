# Rubi Auto Mining Bot

A script that automates daily mining on the Rubi app, eliminating the need for manual clicks. It supports both Android (via Termux) and Windows.


## Features
✅ Automates daily mining  
✅ Works on Android (Termux) & Windows  
✅ Runs in the background  
✅ Supports multiple account   
✅ Lightweight & easy to use  
✅ Saves access tokens and refresh tokens for re-login without needing username and password after the first login
✅ Supports **SOCKS** and **HTTP** proxies  

## Installation  

### For Android (Termux)  

1. Install Termux from the Play Store or F-Droid: https://f-droid.org/packages/com.termux/  
2. Open Termux and run:  
```
   pkg update && pkg upgrade  
   pkg install python git  
   git clone https://github.com/khondokerXhasan/Rubi-Miner.git  
   cd Rubi-Miner
   pip install -r requirements.txt  
```
3. Run the script:  
```
   python miner.py  
```

### For Windows  

1. Install Python from https://www.python.org/downloads/ (Make sure to check "Add Python to PATH" during installation).  
2. Download or clone the repository:  
```
   git clone https://github.com/khondokerXhasan/Rubi-Miner.git  
   cd Rubi-Miner  
```
3. Install dependencies:  
```
   pip install -r requirements.txt  
````
4. Run the script:  
```
   python miner.py
```

## Before Running the Script  
Before you run the script, add your accounts to `accounts.txt`. Each account should be listed on a new line in the following format:
```
username|password
username1|password1
username2|password2
```
The script will automatically use the credentials from `accounts.txt` for the initial login attempt.

## How It Works After First Login  
After the first login attempt, the script will save the **access_token** and **refresh_token** in an `accounts.json` file. 

- On subsequent runs, it will use the **access_token** and **refresh_token** from `accounts.json` instead of the username and password, bypassing the login process.
- The script will automatically **refresh the tokens** when needed and dynamically update the `accounts.json` file with the latest tokens.

### Proxy Support (Optional)  
The script supports **SOCKS** and **HTTP** proxies.  

- To use proxies, add them to the `proxies.txt` file, each on a new line in the following format:
```
http://proxy_ip:port
socks5://proxy_ip:port
```
- If no proxy is provided, the script will continue running **without a proxy**.  

## If You Are Not Registered On The Rubi App  
If you haven't registered on the Rubi app yet, follow these steps:  
1. Download the app from the Play Store: [Rubi App on Play Store](https://play.google.com/store/apps/details?id=com.nemoholding.android.rubi)  
2. When signing up, **use the referral code**: `KHONDOKER2` (this is a must).


## Disclaimer  
This script is for educational purposes only. Automating app interactions may violate the app's Terms of Service, which could result in account bans. Use at your own risk.  


## License  
This project is licensed under the MIT License. See the LICENSE file for details.
