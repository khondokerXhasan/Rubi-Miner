# Rubi Auto Mining Bot

A script that automates daily mining on the Rubi app, eliminating the need for manual clicks. It supports both Android (via Termux) and Windows.


## Features
✅ Automates daily mining  
✅ Works on Android (Termux) & Windows  
✅ Runs in the background  
✅ Supports multiple account
✅ Lightweight & easy to use  


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

## If You Are Not Registered On The Rubi App  
If you haven't registered on the Rubi app yet, follow these steps:  
1. Download the app from the Play Store: [Rubi App on Play Store](https://play.google.com/store/apps/details?id=com.nemoholding.android.rubi)  
2. When signing up, **use the referral code**: `KHONDOKER2` (this is a must).


## Disclaimer  
This script is for educational purposes only. Automating app interactions may violate the app's Terms of Service, which could result in account bans. Use at your own risk.  


## License  
This project is licensed under the MIT License. See the LICENSE file for details.
