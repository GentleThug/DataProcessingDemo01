#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: test.py    
@Time: 2021/12/23 11:28 
"""
import json
import random
import time
from hashlib import md5

import requests
from tqdm import tqdm


def translate_weapon_BaiduAPI(text):
    time.sleep(1)

    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    # 设置您自己的 appid appkey
    # appid = '20210103000662608'
    # appkey = 'XjdpSSpFdJ0gEOGy0lO6'

    appid = '20211215001028934'
    appkey = 'NLo0hEf0Dp5feEonwS4K'

    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'

    query = text

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    # Build request构建请求
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    # 中文转英文
    payload = {'appid': appid, 'q': query, 'from': 'en', 'to': 'zh', 'salt': salt, 'sign': sign}

    # Send request发送请求
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()

    # Show response显示回复
    # print(json.dumps(result, indent=4, ensure_ascii=False))
    return result['trans_result'][0].get('dst')


#
def translate(file_name):
    data = []
    count = 0
    content = []
    with open(file_name, 'r', encoding='utf-8') as f:
        file = json.load(f)
    for i in tqdm(file):
        # print(i)
        count += 1
        try:
            title = translate_weapon_BaiduAPI(i)
        except:
            title = ""
            print(count, "False")

        #     dic = {z: title}
        data.append(title)
        # print(json.dumps(data, indent=4, ensure_ascii=False))
    with open('translate_result/单词翻译（2.0）.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    f.close()


if __name__ == '__main__':
    translate('cmano_tilte单词（7189）.json')
    pass