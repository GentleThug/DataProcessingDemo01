# -*- encoding: utf-8 -*-
"""
@File    :   Demo_18_translate.py    
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
    time.sleep(0.5)
    # 设置Google翻译服务地址
    translator = Translator(service_urls=[
        'translate.google.cn'
    ])
    translation = translator.translate(text, dest='zh-CN')
    return translation.text


def translate_baiduAPI(text):
    time.sleep(0.9)
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
    payload = {'appid': appid, 'q': query, 'from': 'en', 'to': 'zh', 'salt': salt, 'sign': sign}
    # payload = {'appid': appid, 'q': query, 'from': 'zh', 'to': 'en', 'salt': salt, 'sign': sign}

    # Send request发送请求
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()

    # Show response显示回复
    # print(json.dumps(result, indent=4, ensure_ascii=False))
    # print(result['trans_result'][0].get('dst'))
    return result['trans_result'][0].get('dst')
# .replace("“", "\"").replace("“", "\"")\
#         .replace("’", "\"").replace("‘", "\"")\
#         .replace("，", ",").replace("”", "\"")\
#         .replace("、", ",").replace("：", ":").replace("'", "\"")
# {'title'：'Harfang无人机[Heron Mod]-2020，3x'，'url'：'http://cmano-db.com/aircraft/5383/“，”国家/类型“：”摩洛哥“，“一般数据：”：[{“类型：”“无人机（UAV）”，“机组人员：”“0”，“最小速度：”“70节”，“最大速度：”“115节”，“翼展：”“16.6米”，“高度：”“0.0米”，“长度：”“9.5米”，“最大有效载荷：”“0千克”，“空重：”“657千克”，“最大重量：”“1250千克”，“操作员：”“空军”，“调试：”“2020”，“推进：”“1x Rotax 914 UL”]，“传感器/电子战：”：[“通用FLIR-（弃用-第三代，监视）红外\n\t\t\t\t\t红外，监视摄像机最大射程：83.3公里”，“通用激光指示器-（仅限地面）激光指示器\n\t\t\t\t激光目标指示器和测距仪（LTD/R）最大射程：18.5公里”，“EL/M-2022U-（无人机变型）雷达\n\t\t\t\t\tRadar，地面搜索，远程最大距离：370.4 km']}

if __name__ == '__main__':
    data = []
    with open('cmano_data/12.15_translate/aircraft_test.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    # with open('cmano_data/12.5cmano_合并/aircraft整合9069.json', 'r', encoding='utf-8') as f:
    #     file = json.load(f)
    for i in tqdm(file):
        # {'title'：'Harfang无人机[Heron Mod]-2020，3x'，'url'：'http://cmano-db.com/aircraft/5383/“，”国家/类型“：”摩洛哥“，“一般数据：”：[{“类型：”“无人机（UAV）”，“机组人员：”“0”，“最小速度：”“70节”，“最大速度：”“115节”，“翼展：”“16.6米”，“高度：”“0.0米”，“长度：”“9.5米”，“最大有效载荷：”“0千克”，“空重：”“657千克”，“最大重量：”“1250千克”，“操作员：”“空军”，“调试：”“2020”，“推进：”“1x Rotax 914 UL”]，“传感器/电子战：”：[“通用FLIR-（弃用-第三代，监视）红外\n\t\t\t\t\t红外，监视摄像机最大射程：83.3公里”，“通用激光指示器-（仅限地面）激光指示器\n\t\t\t\t激光目标指示器和测距仪（LTD/R）最大射程：18.5公里”，“EL/M-2022U-（无人机变型）雷达\n\t\t\t\t\tRadar，地面搜索，远程最大距离：370.4 km']}
        # data.append()
        # data.append(eval(translate_baiduAPI(str(i)).replace("：”", ":'").replace("“", "'").replace("，", ",")))
        print(translate_baiduAPI(str(i)))



    with open('cmano_data/12.15_translate/res_aircraft_test.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    f.close()
