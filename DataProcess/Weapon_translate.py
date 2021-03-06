# -*- encoding: utf-8 -*-
"""
@File    :   Weapon_translate.py    
@Contact :   wu466687121@qq.com
@License :   (C)Copyright 2020-2021

    @Modify Time       @Author    @Version   @Desciption
-------------------   ---------   ---------   -----------
2021/12/17 上午11:24       SEA         1.0         None
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
    payload = {'appid': appid, 'q': query, 'from': 'zh', 'to': 'en', 'salt': salt, 'sign': sign}

    # Send request发送请求
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()

    # Show response显示回复
    # print(json.dumps(result, indent=4, ensure_ascii=False))
    return result['trans_result'][0].get('dst')

#
def translate_weapon(file_name):
    data = []
    with open('merge_data/12.16/' + file_name, 'r', encoding='utf-8') as f:
        file = json.load(f)
    for i in tqdm(file):
        for j, k in i.items():
            try:
                title = translate_weapon_BaiduAPI(j)
            except:
                title = ""
                print("False")

            dic = {"title": title, j: k}
        data.append(dic)
    with open('merge_data/12.16/translate_result/' + file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    f.close()


if __name__ == '__main__':
    translate_weapon('res_Weapon_data_12.16_3.json')
    pass