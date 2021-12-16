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


def translate(text):
    # 设置Google翻译服务地址
    time.sleep(0.1)
    translator = Translator(service_urls=[
        'translate.google.cn'
    ])
    translation = translator.translate(text, dest='zh-CN')
    return translation.text


if __name__ == '__main__':
    data = []
    with open('cmano_data/origin/submarine全部647.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    for i in tqdm(file):
        data.append(translate(str(i)))

    with open('cmano_data/12.15_translate/res_submarine全部647.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    f.close()