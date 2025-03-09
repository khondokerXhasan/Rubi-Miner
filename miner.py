import requests as _0xf3f48d1f
import json as json
import os as _0xbae22184
import random as _0xb3c387c0
import string as _0x851e4d22
import uuid as _0x48fc5415
from datetime import datetime as _0xa99401a7, timezone as _0x2354cd04
import time as _0x25c12759
import sys as _0xdbb82a5e
_0x5fd834bd = 'https://rubi.click'
_0xe8a977d6 = f'{_0x5fd834bd}/api/home'
_0x98ac3f64 = f'{_0x5fd834bd}/api/login'
_0x84b6ab52 = f'{_0x5fd834bd}/api/user/refresh'
_0xf1590c17 = f'{_0x5fd834bd}/api/exploit/stock_v2'
_0xcaff9542 = f'{_0x5fd834bd}/api/exploit'
_0x190d3efe = f'{_0x5fd834bd}/api/my-profile'
_0xb003a376 = f'{_0x5fd834bd}/api/exploit/time-remain'
_0x125d0fef = 'accounts.json'
_0x0294907f = 'accounts.txt'
_0x08ec9a5a = {'accept': 'application/json', 'lang': 'en', 'driver-login': 'jwt', 'app_version': '1.42', 'Content-Type': 'application/json', 'Host': 'rubi.click', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.9.1'}
_0xe73d184a = [{'name': 'Nexus 5', 'model': 'Nexus 5', 'branch': 'google', 'manufacturer': 'LGE'}, {'name': 'Nexus 6P', 'model': 'Nexus 6P', 'branch': 'google', 'manufacturer': 'Huawei'}, {'name': 'Pixel 3', 'model': 'Pixel 3', 'branch': 'google', 'manufacturer': 'Google'}, {'name': 'Pixel 4a', 'model': 'Pixel 4a', 'branch': 'google', 'manufacturer': 'Google'}, {'name': 'Pixel 6', 'model': 'Pixel 6', 'branch': 'google', 'manufacturer': 'Google'}, {'name': 'Pixel 7 Pro', 'model': 'Pixel 7 Pro', 'branch': 'google', 'manufacturer': 'Google'}, {'name': 'Pixel 8', 'model': 'Pixel 8', 'branch': 'google', 'manufacturer': 'Google'}, {'name': 'Pixel 9', 'model': 'Pixel 9', 'branch': 'google', 'manufacturer': 'Google'}, {'name': 'Pixel Fold', 'model': 'Pixel Fold', 'branch': 'google', 'manufacturer': 'Google'}, {'name': 'Galaxy S8', 'model': 'SM-G950F', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Galaxy S10', 'model': 'SM-G973F', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Galaxy S21', 'model': 'SM-G991B', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Galaxy S22 Ultra', 'model': 'SM-S908B', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Galaxy S23', 'model': 'SM-S911B', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Galaxy S24', 'model': 'SM-S921B', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Galaxy Note 20', 'model': 'SM-N981B', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Galaxy A52', 'model': 'SM-A525F', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Galaxy A54', 'model': 'SM-A546B', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Galaxy Z Fold 5', 'model': 'SM-F946B', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Galaxy Z Flip 6', 'model': 'SM-F741B', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Redmi Note 9', 'model': 'Redmi Note 9', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}, {'name': 'Redmi Note 10', 'model': 'Redmi Note 10', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}, {'name': 'Redmi Note 12', 'model': 'Redmi Note 12', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}, {'name': 'Mi 11', 'model': 'Mi 11', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}, {'name': 'Mi 12 Pro', 'model': 'Mi 12 Pro', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}, {'name': 'Xiaomi 13', 'model': 'Xiaomi 13', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}, {'name': 'Xiaomi 14', 'model': 'Xiaomi 14', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}, {'name': 'Poco X3', 'model': 'Poco X3 NFC', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}, {'name': 'Poco F5', 'model': 'Poco F5', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}, {'name': 'Mi 9T', 'model': 'Mi 9T', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}, {'name': 'OnePlus 7T', 'model': 'HD1903', 'branch': 'oneplus', 'manufacturer': 'OnePlus'}, {'name': 'OnePlus 9', 'model': 'LE2110', 'branch': 'oneplus', 'manufacturer': 'OnePlus'}, {'name': 'OnePlus 10 Pro', 'model': 'NE2210', 'branch': 'oneplus', 'manufacturer': 'OnePlus'}, {'name': 'OnePlus 11', 'model': 'PHB110', 'branch': 'oneplus', 'manufacturer': 'OnePlus'}, {'name': 'OnePlus Nord', 'model': 'AC2003', 'branch': 'oneplus', 'manufacturer': 'OnePlus'}, {'name': 'OnePlus Nord 3', 'model': 'CPH2491', 'branch': 'oneplus', 'manufacturer': 'OnePlus'}, {'name': 'Moto G Power', 'model': 'Moto G Power', 'branch': 'motorola', 'manufacturer': 'Motorola'}, {'name': 'Moto Edge 20', 'model': 'XT2143-1', 'branch': 'motorola', 'manufacturer': 'Motorola'}, {'name': 'Moto Edge 40', 'model': 'XT2303-1', 'branch': 'motorola', 'manufacturer': 'Motorola'}, {'name': 'Moto Razr 2023', 'model': 'XT2321-1', 'branch': 'motorola', 'manufacturer': 'Motorola'}, {'name': 'Huawei P30', 'model': 'ELE-L29', 'branch': 'huawei', 'manufacturer': 'Huawei'}, {'name': 'Huawei Mate 40', 'model': 'NOH-NX9', 'branch': 'huawei', 'manufacturer': 'Huawei'}, {'name': 'Huawei P50', 'model': 'ABR-AL00', 'branch': 'huawei', 'manufacturer': 'Huawei'}, {'name': 'Huawei Mate 60', 'model': 'ALN-AL80', 'branch': 'huawei', 'manufacturer': 'Huawei'}, {'name': 'Oppo Find X3', 'model': 'CPH2173', 'branch': 'oppo', 'manufacturer': 'Oppo'}, {'name': 'Oppo Reno 6', 'model': 'CPH2251', 'branch': 'oppo', 'manufacturer': 'Oppo'}, {'name': 'Oppo Find X5 Pro', 'model': 'CPH2305', 'branch': 'oppo', 'manufacturer': 'Oppo'}, {'name': 'Oppo Reno 10', 'model': 'CPH2531', 'branch': 'oppo', 'manufacturer': 'Oppo'}, {'name': 'Vivo Y70', 'model': 'Vivo Y70', 'branch': 'vivo', 'manufacturer': 'Vivo'}, {'name': 'Vivo X60', 'model': 'V2045', 'branch': 'vivo', 'manufacturer': 'Vivo'}, {'name': 'Vivo X90', 'model': 'V2241A', 'branch': 'vivo', 'manufacturer': 'Vivo'}, {'name': 'Vivo Y100', 'model': 'V2239', 'branch': 'vivo', 'manufacturer': 'Vivo'}, {'name': 'Sony Xperia 1 II', 'model': 'XQ-AT52', 'branch': 'sony', 'manufacturer': 'Sony'}, {'name': 'Sony Xperia 5 III', 'model': 'XQ-BQ72', 'branch': 'sony', 'manufacturer': 'Sony'}, {'name': 'Sony Xperia 1 V', 'model': 'XQ-DQ72', 'branch': 'sony', 'manufacturer': 'Sony'}, {'name': 'Sony Xperia 10 VI', 'model': 'XQ-ES52', 'branch': 'sony', 'manufacturer': 'Sony'}, {'name': 'Realme 8', 'model': 'RMX3085', 'branch': 'realme', 'manufacturer': 'Realme'}, {'name': 'Realme GT', 'model': 'RMX2202', 'branch': 'realme', 'manufacturer': 'Realme'}, {'name': 'Realme GT 3', 'model': 'RMX3709', 'branch': 'realme', 'manufacturer': 'Realme'}, {'name': 'Realme Narzo 60', 'model': 'RMX3750', 'branch': 'realme', 'manufacturer': 'Realme'}, {'name': 'Asus ROG Phone 7', 'model': 'AI2205', 'branch': 'asus', 'manufacturer': 'Asus'}, {'name': 'Nokia G60', 'model': 'TA-1479', 'branch': 'nokia', 'manufacturer': 'HMD Global'}, {'name': 'Nothing Phone (2)', 'model': 'A065', 'branch': 'nothing', 'manufacturer': 'Nothing'}, {'name': 'Lenovo Legion Phone Duel 2', 'model': 'L70081', 'branch': 'lenovo', 'manufacturer': 'Lenovo'}, {'name': 'ZTE Axon 40 Ultra', 'model': 'A2022', 'branch': 'zte', 'manufacturer': 'ZTE'}, {'name': 'Galaxy Tab S9', 'model': 'SM-X710', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Xiaomi Pad 6', 'model': 'Xiaomi Pad 6', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}]
_0x035206ee = ['9', '10', '11', '12', '13']

def _0xaa251f51():
    return ''.join(_0xb3c387c0.choices(_0x851e4d22.hexdigits.lower(), k=16))

def _0x5bab050f():
    return str(_0x48fc5415.uuid4())

def _0x9be5f4b2():
    _0xae078d88 = _0xb3c387c0.choice(_0xe73d184a)
    return {'device_push_token': _0x5bab050f(), 'device_os': 'android', 'device_id': _0xaa251f51(), 'device_name': _0xae078d88['name'], 'device_model': _0xae078d88['model'], 'device_branch': _0xae078d88['branch'], 'device_os_version': _0xb3c387c0.choice(_0x035206ee), 'device_manufacturer': _0xae078d88['manufacturer']}

def _0x9f813dc3(_0x203f2bbc):
    return '|'.join([_0x203f2bbc['device_name'], _0x203f2bbc['device_id'], _0x203f2bbc['device_model'], _0x203f2bbc['device_branch'], _0x203f2bbc['device_manufacturer'], _0x203f2bbc['device_os_version'], _0x203f2bbc['device_push_token']])

def _0x362211a6(_0xde15260c):
    _0x85d577ee = _0xde15260c.split('|')
    return {'device_name': _0x85d577ee[0], 'device_id': _0x85d577ee[1], 'device_model': _0x85d577ee[2], 'device_branch': _0x85d577ee[3], 'device_manufacturer': _0x85d577ee[4], 'device_os_version': _0x85d577ee[5], 'device_push_token': _0x85d577ee[6]}

def _0x7acefe53():
    if not _0xbae22184.path.exists(_0x125d0fef):
        print(f'[*] Creating new {_0x125d0fef}')
        with open(_0x125d0fef, 'w') as _0xed6e9dbd:
            json.dump([], _0xed6e9dbd)
        return []
    with open(_0x125d0fef, 'r') as _0xed6e9dbd:
        _0xef3ef966 = json.load(_0xed6e9dbd)
        if not isinstance(_0xef3ef966, list):
            raise Exception(f'{_0x125d0fef} must contain an array of accounts.')
        return _0xef3ef966

def _0x6ecb2ded():
    if not _0xbae22184.path.exists(_0x0294907f):
        print(f'[*] Creating new {_0x0294907f}')
        with open(_0x0294907f, 'w') as _0xed6e9dbd:
            _0xed6e9dbd.write('')
        return []
    with open(_0x0294907f, 'r') as _0xed6e9dbd:
        _0x416ba854 = _0xed6e9dbd.readlines()
        _0xef3ef966 = []
        for _0x929c56ac in _0x416ba854:
            _0x929c56ac = _0x929c56ac.strip()
            if _0x929c56ac and '|' in _0x929c56ac:
                (_0xb32f402c, _0x2bbbe8d2) = _0x929c56ac.split('|', 1)
                _0xef3ef966.append({'username': _0xb32f402c, 'password': _0x2bbbe8d2})
        return _0xef3ef966

def _0xd736be73(_0xef3ef966):
    with open(_0x125d0fef, 'w') as _0xed6e9dbd:
        json.dump(_0xef3ef966, _0xed6e9dbd, indent=4)

def _0xa6779135(_0xb32f402c, _0x2bbbe8d2, _0x203f2bbc=None):
    if _0x203f2bbc is None:
        _0x203f2bbc = _0x9be5f4b2()
    _0x339f6c29 = {'username': _0xb32f402c, 'password': _0x2bbbe8d2, 'device_push_token': _0x203f2bbc['device_push_token'], 'device_os': 'android', 'device_id': _0x203f2bbc['device_id'], 'device_name': _0x203f2bbc['device_name'], 'device_model': _0x203f2bbc['device_model'], 'device_branch': _0x203f2bbc['device_branch'], 'device_os_version': _0x203f2bbc['device_os_version'], 'device_manufacturer': _0x203f2bbc['device_manufacturer']}
    while True:
        _0xda54b85d = _0xf3f48d1f.post(_0x98ac3f64, headers=_0x08ec9a5a, json=_0x339f6c29)
        if _0xda54b85d.status_code not in [502, 500]:
            break
        _0x25c12759.sleep(2)
    if _0xda54b85d.status_code == 200:
        _0xaab8ee1e = _0xda54b85d.json()
        if 'expires_in' not in _0xaab8ee1e:
            raise Exception(f"Login response for {_0xb32f402c} missing 'expires_in' key: {_0xaab8ee1e}")
        _0xaab8ee1e['expires_at'] = int(_0xa99401a7.now().timestamp()) + _0xaab8ee1e['expires_in']
        return (_0xaab8ee1e, _0x203f2bbc)
    else:
        raise Exception(f'Login failed for {_0xb32f402c}: {_0xda54b85d.status_code} - {_0xda54b85d.text}')

def _0xe5dccaaf(_0x9be5c9bf, _0xb32f402c, _0x31e1a6cd):
    _0xc8f3743b = _0x08ec9a5a.copy()
    _0xc8f3743b['authorization'] = f'Bearer {_0x9be5c9bf}'
    while True:
        _0xda54b85d = _0xf3f48d1f.post(_0x84b6ab52, headers=_0xc8f3743b)
        if _0xda54b85d.status_code not in [502, 500]:
            break
        _0x25c12759.sleep(2)
    if _0xda54b85d.status_code == 200:
        _0xaab8ee1e = _0xda54b85d.json()
        if 'expires_in' not in _0xaab8ee1e:
            raise Exception(f"Refresh response for {_0xb32f402c} missing 'expires_in' key: {_0xaab8ee1e}")
        _0xaab8ee1e['expires_at'] = int(_0xa99401a7.now().timestamp()) + _0xaab8ee1e['expires_in']
        for _0xaa5a6fd0 in _0x31e1a6cd:
            if _0xaa5a6fd0.get('username') == _0xb32f402c:
                _0xaa5a6fd0['token_data'] = _0xaab8ee1e
                _0xd736be73(_0x31e1a6cd)
                print(f'[*] Token refreshed and saved for {_0xb32f402c}')
                break
        return _0xaab8ee1e
    else:
        raise Exception(f'Token refresh failed for {_0xb32f402c}: {_0xda54b85d.status_code} - {_0xda54b85d.text}')

def _0x033f4874(_0xa92e5bb9=0):
    _0xa150ef97 = _0xa99401a7.now(_0x2354cd04.utc)
    if _0xa92e5bb9:
        _0xa150ef97 = _0xa150ef97.replace(hour=_0xa150ef97._0x3d2e879d - _0xa92e5bb9)
    return _0xa150ef97.strftime('%a, %d %b %Y %H:%M:%S GMT')

def _0x582f630a(_0x9be5c9bf):
    _0xc8f3743b = _0x08ec9a5a.copy()
    _0xc8f3743b['authorization'] = f'Bearer {_0x9be5c9bf}'
    _0xc8f3743b['If-Modified-Since'] = _0x033f4874()
    while True:
        _0xda54b85d = _0xf3f48d1f.get(_0xf1590c17, headers=_0xc8f3743b)
        if _0xda54b85d.status_code not in [502, 500]:
            break
        _0x25c12759.sleep(2)
    if _0xda54b85d.status_code == 200:
        return _0xda54b85d.json()
    else:
        raise Exception(f'Failed to check stock: {_0xda54b85d.status_code} - {_0xda54b85d.text}')

def _0x2aff58db(_0x9be5c9bf, _0x34aa36af):
    _0xc8f3743b = _0x08ec9a5a.copy()
    _0xc8f3743b['authorization'] = f'Bearer {_0x9be5c9bf}'
    _0x339f6c29 = {'exploit_stock_id': _0x34aa36af}
    while True:
        _0xda54b85d = _0xf3f48d1f.post(_0xcaff9542, headers=_0xc8f3743b, json=_0x339f6c29)
        if _0xda54b85d.status_code not in [502, 500]:
            break
        _0x25c12759.sleep(2)
    if _0xda54b85d.status_code == 200:
        return _0xda54b85d.json()
    else:
        raise Exception(f'Failed to start exploit: {_0xda54b85d.status_code} - {_0xda54b85d.text}')

def _0xde8071fa(_0x9be5c9bf):
    _0xc8f3743b = _0x08ec9a5a.copy()
    _0xc8f3743b['authorization'] = f'Bearer {_0x9be5c9bf}'
    while True:
        _0xda54b85d = _0xf3f48d1f.post(_0xb003a376, headers=_0xc8f3743b)
        if _0xda54b85d.status_code not in [502, 500]:
            break
        _0x25c12759.sleep(2)
    if _0xda54b85d.status_code == 200:
        return _0xda54b85d.json()
    else:
        raise Exception(f'Failed to check time remaining: {_0xda54b85d.status_code} - {_0xda54b85d.text}')

def _0x3d30c654(_0x9be5c9bf):
    _0xc8f3743b = _0x08ec9a5a.copy()
    _0xc8f3743b['authorization'] = f'Bearer {_0x9be5c9bf}'
    _0xc8f3743b['If-Modified-Since'] = _0x033f4874()
    _0x6fc086c3 = {'wallet': '1', 'member_count_in_group': '1'}
    while True:
        _0xda54b85d = _0xf3f48d1f.get(_0x190d3efe, params=_0x6fc086c3, headers=_0xc8f3743b)
        if _0xda54b85d.status_code not in [502, 500]:
            break
        _0x25c12759.sleep(2)
    if _0xda54b85d.status_code == 200:
        return _0xda54b85d.json()
    else:
        raise Exception(f'Failed to get user info: {_0xda54b85d.status_code} - {_0xda54b85d.text}')

def _0xe0a7ce5c(_0x9be5c9bf):
    _0xc8f3743b = _0x08ec9a5a.copy()
    _0xc8f3743b['authorization'] = f'Bearer {_0x9be5c9bf}'
    _0xc8f3743b['If-Modified-Since'] = _0x033f4874()
    while True:
        _0xda54b85d = _0xf3f48d1f.get(_0xe8a977d6, headers=_0xc8f3743b)
        if _0xda54b85d.status_code not in [502, 500]:
            break
        _0x25c12759.sleep(2)
    if _0xda54b85d.status_code == 200:
        return _0xda54b85d.json()
    else:
        raise Exception(f'Failed to go home: {_0xda54b85d.status_code} - {_0xda54b85d.text}')

def _0x2d4c781c(_0xaa5a6fd0, _0x31e1a6cd):
    _0xb32f402c = _0xaa5a6fd0.get('username')
    _0x2bbbe8d2 = _0xaa5a6fd0.get('password')
    for _0x32e47443 in _0x31e1a6cd:
        if _0x32e47443.get('username') == _0xb32f402c:
            _0xaab8ee1e = _0x32e47443.get('token_data', {})
            _0x1aaf6a89 = _0x32e47443.get('device_info')
            if _0xaab8ee1e and 'expires_at' in _0xaab8ee1e:
                if _0xaab8ee1e['expires_at'] > int(_0xa99401a7.now().timestamp()):
                    print(f'[*] Using existing valid token for {_0xb32f402c}')
                    return (_0xaab8ee1e['access_token'], _0x32e47443)
                else:
                    print(f'[*] Token expired for {_0xb32f402c}. Refreshing...')
                    _0x73824b13 = _0xe5dccaaf(_0xaab8ee1e['access_token'], _0xb32f402c, _0x31e1a6cd)
                    return (_0x73824b13['access_token'], _0x32e47443)
    _0x203f2bbc = _0x9be5f4b2()
    (_0xaab8ee1e, _0x203f2bbc) = _0xa6779135(_0xb32f402c, _0x2bbbe8d2, _0x203f2bbc)
    _0x863d20b9 = {'username': _0xb32f402c, 'password': _0x2bbbe8d2, 'device_info': _0x9f813dc3(_0x203f2bbc), 'token_data': _0xaab8ee1e}
    _0x31e1a6cd.append(_0x863d20b9)
    _0xd736be73(_0x31e1a6cd)
    print(f'[*] Initial login completed for {_0xb32f402c}. Device info and token saved.')
    return (_0xaab8ee1e['access_token'], _0x863d20b9)

def _0x862503f8():
    print('\n    ╔════════════════════════════════════════════╗\n    ║                                            ║\n    ║               RUBI AUTO MINER              ║\n    ║         By Github: khondokerXhasan         ║\n    ║                                            ║\n    ╚════════════════════════════════════════════╝\n    ')

def _0xfd8277ad(_0x9e07ba3d):
    while _0x9e07ba3d > 0:
        _0x9489114d = _0x9e07ba3d // 3600
        _0xa86f4f38 = _0x9e07ba3d % 3600 // 60
        _0x6c645a78 = _0x9e07ba3d % 60
        _0xdc345ea9 = f'\r[~] Sleeping: {_0x9489114d:02d}:{_0xa86f4f38:02d}:{_0x6c645a78:02d} remaining'
        _0xdbb82a5e.stdout.write(_0xdc345ea9)
        _0xdbb82a5e.stdout.flush()
        _0x25c12759.sleep(1)
        _0x9e07ba3d -= 1
    _0xdbb82a5e.stdout.write('\r[~] Sleep complete!                \n')
    _0xdbb82a5e.stdout.flush()

def _0x41bf4e9d():
    try:
        while True:
            _0x31e1a6cd = _0x7acefe53()
            _0x0461278f = _0x6ecb2ded()
            _0xab77bcc9 = 86800
            if not _0x0461278f:
                print(f"[!] No accounts found in {_0x0294907f}. Please add accounts in the format 'username|password'.")
                return
            for _0xaa5a6fd0 in _0x0461278f:
                print()
                _0xb32f402c = _0xaa5a6fd0.get('username')
                if not _0xb32f402c or not _0xaa5a6fd0.get('password'):
                    print(f'[!] Skipping account: No username or password provided.')
                    continue
                try:
                    (_0x9be5c9bf, _0x92762fe7) = _0x2d4c781c(_0xaa5a6fd0, _0x31e1a6cd)
                    print(f"[*] '{_0xb32f402c}' Login Successful")
                    _0xcbee0824 = _0x3d30c654(_0x9be5c9bf)
                    _0xb32f402c = _0xcbee0824['data']['username']
                    _0x7979cc2e = _0xcbee0824['data']['email']
                    _0x52db7fef = _0xe0a7ce5c(_0x9be5c9bf)
                    _0xd21b6af9 = _0x52db7fef['data']['info'].get('ruby_block_swap_all', 0)
                    _0x9bf8ad43 = _0x52db7fef['data']['info'].get('exploit_speed', 0)
                    print(f'[*] Username: {_0xb32f402c}\n[*] Email: {_0x7979cc2e}\n[*] Rubi coin: {_0xd21b6af9} (+{_0x9bf8ad43}/day)')
                    _0xe6e7c948 = _0xde8071fa(_0x9be5c9bf)
                    if not _0xe6e7c948.get('data', None):
                        _0xff44ed89 = _0x582f630a(_0x9be5c9bf)
                        _0xc3a94af8 = _0xff44ed89['data']['last_stock']
                        if _0xc3a94af8:
                            name = _0xc3a94af8['name']
                            _0xcbe50231 = _0xc3a94af8['max_exploit']
                            _0xb6e1c6b6 = _0xc3a94af8['current_exploit']
                            _0xfe6aa8da = _0xc3a94af8['status']
                            if _0xb6e1c6b6 >= _0xcbe50231:
                                print(f'[*] Your previous stock `{name}` is now out of stock')
                        _0xf14882d3 = _0xff44ed89['data']['other_stocks']
                        _0xb25ddc47 = _0xf14882d3 + [_0xc3a94af8] if _0xc3a94af8 else _0xf14882d3
                        for _0x1f884300 in _0xb25ddc47:
                            _0x34aa36af = _0x1f884300['id']
                            name = _0x1f884300['name']
                            _0xcbe50231 = _0x1f884300['max_exploit']
                            _0xb6e1c6b6 = _0x1f884300['current_exploit']
                            _0xfe6aa8da = _0x1f884300['status']
                            if _0xfe6aa8da == 'ACTIVE' and _0xb6e1c6b6 < _0xcbe50231:
                                print(f'[*] Available stock found: {name}, exploiting...')
                                _0x93417b92 = _0x2aff58db(_0x9be5c9bf, _0x34aa36af)
                                if _0x93417b92.get('message') == 'success':
                                    print(f'[*] Successfully started mining on {name}')
                                break
                        else:
                            print('[*] No available stocks to exploit.')
                    else:
                        _0xab77bcc9 = _0xe6e7c948['data']['time_remain']
                        print('[*] Mining already in progress...')
                except Exception as e:
                    print(f'[!] Error for {_0xb32f402c}: {str(e)}')
                _0x25c12759.sleep(3)
            sleep = _0xab77bcc9 + _0xb3c387c0.randint(120, 300)
            print()
            _0xfd8277ad(sleep)
    except KeyboardInterrupt:
        print('\n[*] Script interrupted by user.')
    except Exception as e:
        print(f'[!] Main loop error: {str(e)}')
if __name__ == '__main__':
    _0x862503f8()
    _0x41bf4e9d()