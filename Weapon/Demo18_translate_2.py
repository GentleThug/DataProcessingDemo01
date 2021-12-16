# -*- encoding: utf-8 -*-
"""
@File    :   Demo18_translate.py
@Contact :   wu466687121@qq.com
@License :   (C)Copyright 2020-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/15 上午10:23   SEA      1.0         None
"""
import json
import time
from googletrans import Translator
from tqdm import tqdm
import random
import json
from hashlib import md5
import requests


def translate(text):
    time.sleep(1)
    # 设置Google翻译服务地址
    translator = Translator(service_urls=[
        'translate.google.cn'
    ])
    translation = translator.translate(text, dest='zh-CN')
    return translation.text


def translate_baiduAPI(text):
    time.sleep(1)
    def make_md5(s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    # 设置您自己的 appid appkey
    appid = '20210103000662608'
    appkey = 'XjdpSSpFdJ0gEOGy0lO6'

    # appid = '20211215001028934'
    # appkey = 'NLo0hEf0Dp5feEonwS4K'

    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'

    query = text

    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    # Build request构建请求
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': 'en', 'to': 'zh', 'salt': salt, 'sign': sign}

    # Send request发送请求
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()

    # Show response显示回复
    # print(json.dumps(result, indent=4, ensure_ascii=False))
    return result['trans_result'][0].get('dst')

if __name__ == '__main__':
    data = []
    # with open('cmano_data/12.15_translate/aircraft_test.json', 'r', encoding='utf-8') as f:
    #     file = json.load(f)
    with open('cmano_data/12.15_translate/test.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    list1 = translate_baiduAPI(str(file)).replace("“", "\"").replace("”", "\"").replace("，", ",")

    with open('cmano_data/12.15_translate/test_muli.json.json', 'w', encoding='utf-8') as f:
        json.dump(list1, f, indent=4, ensure_ascii=False)
    f.close()