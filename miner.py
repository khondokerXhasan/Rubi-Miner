import requests as _0xd8f8d25e
import json as json
import os as _0x26010182
import random as _0x0d1cf49c
import string as _0x845a1102
import uuid as _0x848a2cc9
from datetime import datetime as _0x3b5bfa63, timezone as _0x78b18f69
import time as _0x363825b4
import sys as _0xdbd001f3
_0x9b6c9ee4 = 'https://rubi.click'
_0x8bb10589 = f'{_0x9b6c9ee4}/api/home'
_0x1d67bbf0 = f'{_0x9b6c9ee4}/api/login'
_0xc2b1db99 = f'{_0x9b6c9ee4}/api/user/refresh'
_0x5b74180f = f'{_0x9b6c9ee4}/api/exploit/stock_v2'
_0x63a8c0c6 = f'{_0x9b6c9ee4}/api/exploit'
_0xd4b7f30b = f'{_0x9b6c9ee4}/api/my-profile'
_0x2bf28c98 = f'{_0x9b6c9ee4}/api/exploit/time-remain'
_0x5600f5fd = 'accounts.json'
_0x4e2c27c8 = 'accounts.txt'
_0x70f8de1f = 'proxies.txt'
_0x5cae82b5 = {'accept': 'application/json', 'lang': 'en', 'driver-login': 'jwt', 'app_version': '1.42', 'Content-Type': 'application/json', 'Host': 'rubi.click', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/4.9.1'}
_0x06f2463f = [{'name': 'Nexus 5', 'model': 'Nexus 5', 'branch': 'google', 'manufacturer': 'LGE'}, {'name': 'Nexus 6P', 'model': 'Nexus 6P', 'branch': 'google', 'manufacturer': 'Huawei'}, {'name': 'Pixel 3', 'model': 'Pixel 3', 'branch': 'google', 'manufacturer': 'Google'}, {'name': 'Pixel 4a', 'model': 'Pixel 4a', 'branch': 'google', 'manufacturer': 'Google'}, {'name': 'Pixel 6', 'model': 'Pixel 6', 'branch': 'google', 'manufacturer': 'Google'}, {'name': 'Pixel 7 Pro', 'model': 'Pixel 7 Pro', 'branch': 'google', 'manufacturer': 'Google'}, {'name': 'Pixel 8', 'model': 'Pixel 8', 'branch': 'google', 'manufacturer': 'Google'}, {'name': 'Pixel 9', 'model': 'Pixel 9', 'branch': 'google', 'manufacturer': 'Google'}, {'name': 'Pixel Fold', 'model': 'Pixel Fold', 'branch': 'google', 'manufacturer': 'Google'}, {'name': 'Galaxy S8', 'model': 'SM-G950F', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Galaxy S10', 'model': 'SM-G973F', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Galaxy S21', 'model': 'SM-G991B', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Galaxy S22 Ultra', 'model': 'SM-S908B', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Galaxy S23', 'model': 'SM-S911B', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Galaxy S24', 'model': 'SM-S921B', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Galaxy Note 20', 'model': 'SM-N981B', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Galaxy A52', 'model': 'SM-A525F', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Galaxy A54', 'model': 'SM-A546B', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Galaxy Z Fold 5', 'model': 'SM-F946B', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Galaxy Z Flip 6', 'model': 'SM-F741B', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Redmi Note 9', 'model': 'Redmi Note 9', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}, {'name': 'Redmi Note 10', 'model': 'Redmi Note 10', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}, {'name': 'Redmi Note 12', 'model': 'Redmi Note 12', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}, {'name': 'Mi 11', 'model': 'Mi 11', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}, {'name': 'Mi 12 Pro', 'model': 'Mi 12 Pro', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}, {'name': 'Xiaomi 13', 'model': 'Xiaomi 13', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}, {'name': 'Xiaomi 14', 'model': 'Xiaomi 14', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}, {'name': 'Poco X3', 'model': 'Poco X3 NFC', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}, {'name': 'Poco F5', 'model': 'Poco F5', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}, {'name': 'Mi 9T', 'model': 'Mi 9T', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}, {'name': 'OnePlus 7T', 'model': 'HD1903', 'branch': 'oneplus', 'manufacturer': 'OnePlus'}, {'name': 'OnePlus 9', 'model': 'LE2110', 'branch': 'oneplus', 'manufacturer': 'OnePlus'}, {'name': 'OnePlus 10 Pro', 'model': 'NE2210', 'branch': 'oneplus', 'manufacturer': 'OnePlus'}, {'name': 'OnePlus 11', 'model': 'PHB110', 'branch': 'oneplus', 'manufacturer': 'OnePlus'}, {'name': 'OnePlus Nord', 'model': 'AC2003', 'branch': 'oneplus', 'manufacturer': 'OnePlus'}, {'name': 'OnePlus Nord 3', 'model': 'CPH2491', 'branch': 'oneplus', 'manufacturer': 'OnePlus'}, {'name': 'Moto G Power', 'model': 'Moto G Power', 'branch': 'motorola', 'manufacturer': 'Motorola'}, {'name': 'Moto Edge 20', 'model': 'XT2143-1', 'branch': 'motorola', 'manufacturer': 'Motorola'}, {'name': 'Moto Edge 40', 'model': 'XT2303-1', 'branch': 'motorola', 'manufacturer': 'Motorola'}, {'name': 'Moto Razr 2023', 'model': 'XT2321-1', 'branch': 'motorola', 'manufacturer': 'Motorola'}, {'name': 'Huawei P30', 'model': 'ELE-L29', 'branch': 'huawei', 'manufacturer': 'Huawei'}, {'name': 'Huawei Mate 40', 'model': 'NOH-NX9', 'branch': 'huawei', 'manufacturer': 'Huawei'}, {'name': 'Huawei P50', 'model': 'ABR-AL00', 'branch': 'huawei', 'manufacturer': 'Huawei'}, {'name': 'Huawei Mate 60', 'model': 'ALN-AL80', 'branch': 'huawei', 'manufacturer': 'Huawei'}, {'name': 'Oppo Find X3', 'model': 'CPH2173', 'branch': 'oppo', 'manufacturer': 'Oppo'}, {'name': 'Oppo Reno 6', 'model': 'CPH2251', 'branch': 'oppo', 'manufacturer': 'Oppo'}, {'name': 'Oppo Find X5 Pro', 'model': 'CPH2305', 'branch': 'oppo', 'manufacturer': 'Oppo'}, {'name': 'Oppo Reno 10', 'model': 'CPH2531', 'branch': 'oppo', 'manufacturer': 'Oppo'}, {'name': 'Vivo Y70', 'model': 'Vivo Y70', 'branch': 'vivo', 'manufacturer': 'Vivo'}, {'name': 'Vivo X60', 'model': 'V2045', 'branch': 'vivo', 'manufacturer': 'Vivo'}, {'name': 'Vivo X90', 'model': 'V2241A', 'branch': 'vivo', 'manufacturer': 'Vivo'}, {'name': 'Vivo Y100', 'model': 'V2239', 'branch': 'vivo', 'manufacturer': 'Vivo'}, {'name': 'Sony Xperia 1 II', 'model': 'XQ-AT52', 'branch': 'sony', 'manufacturer': 'Sony'}, {'name': 'Sony Xperia 5 III', 'model': 'XQ-BQ72', 'branch': 'sony', 'manufacturer': 'Sony'}, {'name': 'Sony Xperia 1 V', 'model': 'XQ-DQ72', 'branch': 'sony', 'manufacturer': 'Sony'}, {'name': 'Sony Xperia 10 VI', 'model': 'XQ-ES52', 'branch': 'sony', 'manufacturer': 'Sony'}, {'name': 'Realme 8', 'model': 'RMX3085', 'branch': 'realme', 'manufacturer': 'Realme'}, {'name': 'Realme GT', 'model': 'RMX2202', 'branch': 'realme', 'manufacturer': 'Realme'}, {'name': 'Realme GT 3', 'model': 'RMX3709', 'branch': 'realme', 'manufacturer': 'Realme'}, {'name': 'Realme Narzo 60', 'model': 'RMX3750', 'branch': 'realme', 'manufacturer': 'Realme'}, {'name': 'Asus ROG Phone 7', 'model': 'AI2205', 'branch': 'asus', 'manufacturer': 'Asus'}, {'name': 'Nokia G60', 'model': 'TA-1479', 'branch': 'nokia', 'manufacturer': 'HMD Global'}, {'name': 'Nothing Phone (2)', 'model': 'A065', 'branch': 'nothing', 'manufacturer': 'Nothing'}, {'name': 'Lenovo Legion Phone Duel 2', 'model': 'L70081', 'branch': 'lenovo', 'manufacturer': 'Lenovo'}, {'name': 'ZTE Axon 40 Ultra', 'model': 'A2022', 'branch': 'zte', 'manufacturer': 'ZTE'}, {'name': 'Galaxy Tab S9', 'model': 'SM-X710', 'branch': 'samsung', 'manufacturer': 'Samsung'}, {'name': 'Xiaomi Pad 6', 'model': 'Xiaomi Pad 6', 'branch': 'xiaomi', 'manufacturer': 'Xiaomi'}]
_0xf834ce9c = ['9', '10', '11', '12', '13']

def _0xb9240a3c():
    return ''.join(_0x0d1cf49c.choices(_0x845a1102.hexdigits.lower(), k=16))

def _0x87a5e2a5():
    return str(_0x848a2cc9.uuid4())

def _0x8e4cc205():
    _0x6702c99c = _0x0d1cf49c.choice(_0x06f2463f)
    return {'device_push_token': _0x87a5e2a5(), 'device_os': 'android', 'device_id': _0xb9240a3c(), 'device_name': _0x6702c99c['name'], 'device_model': _0x6702c99c['model'], 'device_branch': _0x6702c99c['branch'], 'device_os_version': _0x0d1cf49c.choice(_0xf834ce9c), 'device_manufacturer': _0x6702c99c['manufacturer']}

def _0x5901a662(_0x9857490d):
    return '|'.join([_0x9857490d['device_name'], _0x9857490d['device_id'], _0x9857490d['device_model'], _0x9857490d['device_branch'], _0x9857490d['device_manufacturer'], _0x9857490d['device_os_version'], _0x9857490d['device_push_token']])

def _0xf2f7eace(_0x7a92b5a1):
    _0xe6a2bea6 = _0x7a92b5a1.split('|')
    return {'device_name': _0xe6a2bea6[0], 'device_id': _0xe6a2bea6[1], 'device_model': _0xe6a2bea6[2], 'device_branch': _0xe6a2bea6[3], 'device_manufacturer': _0xe6a2bea6[4], 'device_os_version': _0xe6a2bea6[5], 'device_push_token': _0xe6a2bea6[6]}

def _0xec61def5():
    if not _0x26010182.path.exists(_0x70f8de1f):
        print(f'[*] No {_0x70f8de1f} file found. Continuing without proxy.')
        return []
    with open(_0x70f8de1f, 'r') as _0xd9f42933:
        _0x96f27262 = [_0xf237291f.strip() for _0xf237291f in _0xd9f42933.readlines() if _0xf237291f.strip()]
    if not _0x96f27262:
        print(f'[*] {_0x70f8de1f} is empty. Continuing without proxy.')
    return _0x96f27262

def _0xc1447af1(_0x5aba30cf):
    if not _0x5aba30cf:
        return None
    _0xc71f27c8 = _0x0d1cf49c.choice(_0x5aba30cf)
    if _0xc71f27c8.startswith('http://'):
        _0x0f4cc8d7 = 'http'
        _0xc71f27c8 = _0xc71f27c8.replace('http://', '')
    elif _0xc71f27c8.startswith('socks5://'):
        _0x0f4cc8d7 = 'socks5'
        _0xc71f27c8 = _0xc71f27c8.replace('socks5://', '')
    elif _0xc71f27c8.startswith('socks4://'):
        _0x0f4cc8d7 = 'socks4'
        _0xc71f27c8 = _0xc71f27c8.replace('socks4://', '')
    else:
        _0x0f4cc8d7 = 'http'
    if '@' in _0xc71f27c8:
        (auth, _0x4815c581) = _0xc71f27c8.split('@', 1)
        (_0x1c423107, _0x7dfb7d62) = auth.split(':', 1)
        (_0xacd1ad5d, _0x15887ac8) = _0x4815c581.split(':', 1)
        _0x34b8c072 = f'{_0x0f4cc8d7}://{_0x1c423107}:{_0x7dfb7d62}@{_0xacd1ad5d}:{_0x15887ac8}'
    else:
        (_0xacd1ad5d, _0x15887ac8) = _0xc71f27c8.split(':', 1)
        _0x34b8c072 = f'{_0x0f4cc8d7}://{_0xacd1ad5d}:{_0x15887ac8}'
    if _0x0f4cc8d7 == 'http':
        return {'http': _0x34b8c072, 'https': _0x34b8c072}
    elif _0x0f4cc8d7 in ['socks4', 'socks5']:
        return {'http': _0x34b8c072, 'https': _0x34b8c072}
    else:
        raise ValueError(f'Unsupported proxy scheme: {_0x0f4cc8d7}')

def _0x1d79182c():
    if not _0x26010182.path.exists(_0x5600f5fd):
        print(f'[*] Creating new {_0x5600f5fd}')
        with open(_0x5600f5fd, 'w') as _0xd9f42933:
            json.dump([], _0xd9f42933)
        return []
    with open(_0x5600f5fd, 'r') as _0xd9f42933:
        _0x02e2d2fa = json.load(_0xd9f42933)
        if not isinstance(_0x02e2d2fa, list):
            raise Exception(f'{_0x5600f5fd} must contain an array of accounts.')
        return _0x02e2d2fa

def _0xf41e654d():
    if not _0x26010182.path.exists(_0x4e2c27c8):
        print(f'[*] Creating new {_0x4e2c27c8}')
        with open(_0x4e2c27c8, 'w') as _0xd9f42933:
            _0xd9f42933.write('')
        return []
    with open(_0x4e2c27c8, 'r') as _0xd9f42933:
        _0x05c69b3d = _0xd9f42933.readlines()
        _0x02e2d2fa = []
        for _0xf237291f in _0x05c69b3d:
            _0xf237291f = _0xf237291f.strip()
            if _0xf237291f and '|' in _0xf237291f:
                (_0x1c423107, _0x7dfb7d62) = _0xf237291f.split('|', 1)
                _0x02e2d2fa.append({'username': _0x1c423107, 'password': _0x7dfb7d62})
        return _0x02e2d2fa

def _0xd7a63a50(_0x02e2d2fa):
    with open(_0x5600f5fd, 'w') as _0xd9f42933:
        json.dump(_0x02e2d2fa, _0xd9f42933, indent=4)

def _0x95cce8a2(_0x1c423107, _0x7dfb7d62, _0x9857490d=None, _0x8d1749d5=None):
    if _0x9857490d is None:
        _0x9857490d = _0x8e4cc205()
    _0x75007123 = {'username': _0x1c423107, 'password': _0x7dfb7d62, 'device_push_token': _0x9857490d['device_push_token'], 'device_os': 'android', 'device_id': _0x9857490d['device_id'], 'device_name': _0x9857490d['device_name'], 'device_model': _0x9857490d['device_model'], 'device_branch': _0x9857490d['device_branch'], 'device_os_version': _0x9857490d['device_os_version'], 'device_manufacturer': _0x9857490d['device_manufacturer']}
    while True:
        try:
            _0x645f222f = _0xd8f8d25e.post(_0x1d67bbf0, headers=_0x5cae82b5, json=_0x75007123, proxies=_0x8d1749d5, timeout=10)
            if _0x645f222f.status_code not in [502, 500]:
                break
        except _0xd8f8d25e.exceptions.RequestException as e:
            print(f'[!] Proxy error during login: {str(e)}. Retrying...')
        _0x363825b4.sleep(2)
    if _0x645f222f.status_code == 200:
        _0x6f8046e0 = _0x645f222f.json()
        if 'expires_in' not in _0x6f8046e0:
            raise Exception(f"Login response for {_0x1c423107} missing 'expires_in' key: {_0x6f8046e0}")
        _0x6f8046e0['expires_at'] = int(_0x3b5bfa63.now().timestamp()) + _0x6f8046e0['expires_in']
        return (_0x6f8046e0, _0x9857490d)
    else:
        raise Exception(f'Login failed for {_0x1c423107}: {_0x645f222f.status_code} - {_0x645f222f.text}')

def _0xfa536a16(_0xbf66b8f3, _0x1c423107, _0x3532a147, _0x8d1749d5=None):
    _0xc64e7e33 = _0x5cae82b5.copy()
    _0xc64e7e33['authorization'] = f'Bearer {_0xbf66b8f3}'
    while True:
        try:
            _0x645f222f = _0xd8f8d25e.post(_0xc2b1db99, headers=_0xc64e7e33, proxies=_0x8d1749d5, timeout=10)
            if _0x645f222f.status_code not in [502, 500]:
                break
        except _0xd8f8d25e.exceptions.RequestException as e:
            print(f'[!] Proxy error during token refresh: {str(e)}. Retrying...')
        _0x363825b4.sleep(2)
    if _0x645f222f.status_code == 200:
        _0x6f8046e0 = _0x645f222f.json()
        if 'expires_in' not in _0x6f8046e0:
            raise Exception(f"Refresh response for {_0x1c423107} missing 'expires_in' key: {_0x6f8046e0}")
        _0x6f8046e0['expires_at'] = int(_0x3b5bfa63.now().timestamp()) + _0x6f8046e0['expires_in']
        for _0x87532bcf in _0x3532a147:
            if _0x87532bcf.get('username') == _0x1c423107:
                _0x87532bcf['token_data'] = _0x6f8046e0
                _0xd7a63a50(_0x3532a147)
                print(f'[*] Token refreshed and saved for {_0x1c423107}')
                break
        return _0x6f8046e0
    else:
        raise Exception(f'Token refresh failed for {_0x1c423107}: {_0x645f222f.status_code} - {_0x645f222f.text}')

def _0x6c7bd227(_0x21dec91f=0):
    _0xd7e04e1b = _0x3b5bfa63.now(_0x78b18f69.utc)
    if _0x21dec91f:
        _0xd7e04e1b = _0xd7e04e1b.replace(hour=_0xd7e04e1b._0x1b2670c6 - _0x21dec91f)
    return _0xd7e04e1b.strftime('%a, %d %b %Y %H:%M:%S GMT')

def _0x9b4d0f04(_0xbf66b8f3, _0x8d1749d5=None):
    _0xc64e7e33 = _0x5cae82b5.copy()
    _0xc64e7e33['authorization'] = f'Bearer {_0xbf66b8f3}'
    _0xc64e7e33['If-Modified-Since'] = _0x6c7bd227()
    while True:
        try:
            _0x645f222f = _0xd8f8d25e.get(_0x5b74180f, headers=_0xc64e7e33, proxies=_0x8d1749d5, timeout=10)
            if _0x645f222f.status_code not in [502, 500]:
                break
        except _0xd8f8d25e.exceptions.RequestException as e:
            print(f'[!] Proxy error during stock check: {str(e)}. Retrying...')
        _0x363825b4.sleep(2)
    if _0x645f222f.status_code == 200:
        return _0x645f222f.json()
    else:
        raise Exception(f'Failed to check stock: {_0x645f222f.status_code} - {_0x645f222f.text}')

def _0xc4a6474d(_0xbf66b8f3, _0x891bc495, _0x8d1749d5=None):
    _0xc64e7e33 = _0x5cae82b5.copy()
    _0xc64e7e33['authorization'] = f'Bearer {_0xbf66b8f3}'
    _0x75007123 = {'exploit_stock_id': _0x891bc495}
    while True:
        try:
            _0x645f222f = _0xd8f8d25e.post(_0x63a8c0c6, headers=_0xc64e7e33, json=_0x75007123, proxies=_0x8d1749d5, timeout=10)
            if _0x645f222f.status_code not in [502, 500]:
                break
        except _0xd8f8d25e.exceptions.RequestException as e:
            print(f'[!] Proxy error during exploit start: {str(e)}. Retrying...')
        _0x363825b4.sleep(2)
    if _0x645f222f.status_code == 200:
        return _0x645f222f.json()
    else:
        raise Exception(f'Failed to start exploit: {_0x645f222f.status_code} - {_0x645f222f.text}')

def _0x8b4e2d8a(_0xbf66b8f3, _0x8d1749d5=None):
    _0xc64e7e33 = _0x5cae82b5.copy()
    _0xc64e7e33['authorization'] = f'Bearer {_0xbf66b8f3}'
    while True:
        try:
            _0x645f222f = _0xd8f8d25e.post(_0x2bf28c98, headers=_0xc64e7e33, proxies=_0x8d1749d5, timeout=10)
            if _0x645f222f.status_code not in [502, 500]:
                break
        except _0xd8f8d25e.exceptions.RequestException as e:
            print(f'[!] Proxy error during time remain check: {str(e)}. Retrying...')
        _0x363825b4.sleep(2)
    if _0x645f222f.status_code == 200:
        return _0x645f222f.json()
    else:
        raise Exception(f'Failed to check time remaining: {_0x645f222f.status_code} - {_0x645f222f.text}')

def _0x4baa0da1(_0xbf66b8f3, _0x8d1749d5=None):
    _0xc64e7e33 = _0x5cae82b5.copy()
    _0xc64e7e33['authorization'] = f'Bearer {_0xbf66b8f3}'
    _0xc64e7e33['If-Modified-Since'] = _0x6c7bd227()
    _0xdc18697b = {'wallet': '1', 'member_count_in_group': '1'}
    while True:
        try:
            _0x645f222f = _0xd8f8d25e.get(_0xd4b7f30b, params=_0xdc18697b, headers=_0xc64e7e33, proxies=_0x8d1749d5, timeout=10)
            if _0x645f222f.status_code not in [502, 500]:
                break
        except _0xd8f8d25e.exceptions.RequestException as e:
            print(f'[!] Proxy error during user info check: {str(e)}. Retrying...')
        _0x363825b4.sleep(2)
    if _0x645f222f.status_code == 200:
        return _0x645f222f.json()
    else:
        raise Exception(f'Failed to get user info: {_0x645f222f.status_code} - {_0x645f222f.text}')

def _0x81b223cf(_0xbf66b8f3, _0x8d1749d5=None):
    _0xc64e7e33 = _0x5cae82b5.copy()
    _0xc64e7e33['authorization'] = f'Bearer {_0xbf66b8f3}'
    _0xc64e7e33['If-Modified-Since'] = _0x6c7bd227()
    while True:
        try:
            _0x645f222f = _0xd8f8d25e.get(_0x8bb10589, headers=_0xc64e7e33, proxies=_0x8d1749d5, timeout=10)
            if _0x645f222f.status_code not in [502, 500]:
                break
        except _0xd8f8d25e.exceptions.RequestException as e:
            print(f'[!] Proxy error during go home: {str(e)}. Retrying...')
        _0x363825b4.sleep(2)
    if _0x645f222f.status_code == 200:
        return _0x645f222f.json()
    else:
        raise Exception(f'Failed to go home: {_0x645f222f.status_code} - {_0x645f222f.text}')

def _0xbf5848d3(_0x87532bcf, _0x3532a147, _0x8d1749d5=None):
    _0x1c423107 = _0x87532bcf.get('username')
    _0x7dfb7d62 = _0x87532bcf.get('password')
    for _0x54953d76 in _0x3532a147:
        if _0x54953d76.get('username') == _0x1c423107:
            _0x6f8046e0 = _0x54953d76.get('token_data', {})
            _0xef6f5846 = _0x54953d76.get('device_info')
            if _0x6f8046e0 and 'expires_at' in _0x6f8046e0:
                if _0x6f8046e0['expires_at'] > int(_0x3b5bfa63.now().timestamp()):
                    print(f'[*] Using existing valid token for {_0x1c423107}')
                    return (_0x6f8046e0['access_token'], _0x54953d76)
                else:
                    print(f'[*] Token expired for {_0x1c423107}. Refreshing...')
                    _0x6062b688 = _0xfa536a16(_0x6f8046e0['access_token'], _0x1c423107, _0x3532a147, _0x8d1749d5)
                    return (_0x6062b688['access_token'], _0x54953d76)
    _0x9857490d = _0x8e4cc205()
    (_0x6f8046e0, _0x9857490d) = _0x95cce8a2(_0x1c423107, _0x7dfb7d62, _0x9857490d, _0x8d1749d5)
    _0x5ee517ae = {'username': _0x1c423107, 'password': _0x7dfb7d62, 'device_info': _0x5901a662(_0x9857490d), 'token_data': _0x6f8046e0}
    _0x3532a147.append(_0x5ee517ae)
    _0xd7a63a50(_0x3532a147)
    print(f'[*] Initial login completed for {_0x1c423107}. Device info and token saved.')
    return (_0x6f8046e0['access_token'], _0x5ee517ae)

def _0xc97c151a():
    print('\n    ╔════════════════════════════════════════════╗\n    ║                                            ║\n    ║               RUBI AUTO MINER              ║\n    ║         By Github: khondokerXhasan         ║\n    ║                                            ║\n    ╚════════════════════════════════════════════╝\n    ')

def _0x2279e98b(_0x58d691b8):
    while _0x58d691b8 > 0:
        _0x1159c209 = _0x58d691b8 // 3600
        _0x103893a8 = _0x58d691b8 % 3600 // 60
        _0x5390f478 = _0x58d691b8 % 60
        _0x9863d2ff = f'\r[~] Sleeping: {_0x1159c209:02d}:{_0x103893a8:02d}:{_0x5390f478:02d} remaining'
        _0xdbd001f3.stdout.write(_0x9863d2ff)
        _0xdbd001f3.stdout.flush()
        _0x363825b4.sleep(1)
        _0x58d691b8 -= 1
    _0xdbd001f3.stdout.write('\r[~] Sleep complete!                \n')
    _0xdbd001f3.stdout.flush()

def _0xd463c024():
    try:
        _0x96f27262 = _0xec61def5()
        while True:
            _0x3532a147 = _0x1d79182c()
            _0x42a57882 = _0xf41e654d()
            _0x0878662a = 86800
            if not _0x42a57882:
                print(f"[!] No accounts found in {_0x4e2c27c8}. Please add accounts in the format 'username|password'.")
                return
            for _0x87532bcf in _0x42a57882:
                print()
                _0x1c423107 = _0x87532bcf.get('username')
                if not _0x1c423107 or not _0x87532bcf.get('password'):
                    print(f'[!] Skipping account: No username or password provided.')
                    continue
                _0x8d1749d5 = _0xc1447af1(_0x96f27262)
                if _0x8d1749d5:
                    print(f"[*] Using proxy: {_0x8d1749d5['http']}")
                else:
                    print(f'[*] Running without proxy')
                try:
                    (_0xbf66b8f3, _0xee5ff5f4) = _0xbf5848d3(_0x87532bcf, _0x3532a147, _0x8d1749d5)
                    print(f"[*] '{_0x1c423107}' Login Successful")
                    _0xccf8e97e = _0x4baa0da1(_0xbf66b8f3, _0x8d1749d5)
                    _0x1c423107 = _0xccf8e97e['data']['username']
                    _0xdcff9f96 = _0xccf8e97e['data']['email']
                    _0xe37a3921 = _0x81b223cf(_0xbf66b8f3, _0x8d1749d5)
                    _0x742c0c8c = _0xe37a3921['data']['info'].get('ruby_block_swap_all', 0)
                    _0xeec0a96e = _0xe37a3921['data']['info'].get('exploit_speed', 0)
                    print(f'[*] Username: {_0x1c423107}\n[*] Email: {_0xdcff9f96}\n[*] Rubi coin: {_0x742c0c8c} (+{_0xeec0a96e}/day)')
                    _0xff773647 = _0x8b4e2d8a(_0xbf66b8f3, _0x8d1749d5)
                    if not _0xff773647.get('data', None):
                        _0x2cff60f6 = _0x9b4d0f04(_0xbf66b8f3, _0x8d1749d5)
                        _0x5854625d = _0x2cff60f6['data']['last_stock']
                        if _0x5854625d:
                            name = _0x5854625d['name']
                            _0x56612152 = _0x5854625d['max_exploit']
                            _0xe89d8ad8 = _0x5854625d['current_exploit']
                            _0x195649ba = _0x5854625d['status']
                            if _0xe89d8ad8 >= _0x56612152:
                                print(f'[*] Your previous stock `{name}` is now out of stock')
                        _0x657e29e5 = _0x2cff60f6['data']['other_stocks']
                        _0x9f4b1984 = _0x657e29e5 + [_0x5854625d] if _0x5854625d else _0x657e29e5
                        for _0x0f07350e in _0x9f4b1984:
                            _0x891bc495 = _0x0f07350e['id']
                            name = _0x0f07350e['name']
                            _0x56612152 = _0x0f07350e['max_exploit']
                            _0xe89d8ad8 = _0x0f07350e['current_exploit']
                            _0x195649ba = _0x0f07350e['status']
                            if _0x195649ba == 'ACTIVE' and _0xe89d8ad8 < _0x56612152:
                                print(f'[*] Available stock found: {name}, exploiting...')
                                _0xd1fca52a = _0xc4a6474d(_0xbf66b8f3, _0x891bc495, _0x8d1749d5)
                                if _0xd1fca52a.get('message') == 'success':
                                    print(f'[*] Successfully started mining on {name}')
                                break
                        else:
                            print('[*] No available stocks to exploit.')
                    else:
                        _0x0878662a = _0xff773647['data']['time_remain']
                        print('[*] Mining already in progress...')
                except Exception as e:
                    print(f'[!] Error for {_0x1c423107}: {str(e)}')
                _0x363825b4.sleep(3)
                print('-' * 50)
            sleep = _0x0878662a + _0x0d1cf49c.randint(120, 300)
            print()
            _0x2279e98b(sleep)
    except KeyboardInterrupt:
        print('\n[*] Script interrupted by user.')
    except Exception as e:
        print(f'[!] Main loop error: {str(e)}')
if __name__ == '__main__':
    _0xc97c151a()
    _0xd463c024()
