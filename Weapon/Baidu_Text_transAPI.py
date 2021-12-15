# -*- coding: utf-8 -*-import requests
import random
import json
from hashlib import md5

import requests


def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()


# 设置您自己的 appid appkey
appid = '20210103000662608'
appkey = 'XjdpSSpFdJ0gEOGy0lO6'

url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'

query = 'Hello World! This is 1st paragraph.\nThis is 2nd paragraph.'

salt = random.randint(32768, 65536)
sign = make_md5(appid + query + str(salt) + appkey)

# Build request构建请求
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
payload = {'appid': appid, 'q': query, 'from': 'en', 'to': 'zh', 'salt': salt, 'sign': sign}

# Send request发送请求
r = requests.post(url, params=payload, headers=headers)
result = r.json()

# Show response显示回复
print(json.dumps(result, indent=4, ensure_ascii=False))
