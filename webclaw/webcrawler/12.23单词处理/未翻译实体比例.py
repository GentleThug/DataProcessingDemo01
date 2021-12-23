#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 未翻译实体比例.py    
@Time: 2021/12/23 19:28 
"""
import json
def compare(filename):

    for i in filename:
        print(i)


if __name__ == '__main__':
    with open("translate_result/name/实体翻译有道1.0.json", 'r', encoding='utf-8') as f:
        youdao = json.load(f)
    with open("translate_result/name/实体翻译百度（1.0）.json", 'r', encoding='utf-8') as f:
        baidu = json.load(f)
    with open("translate_result/name/实体翻译谷歌1.0.json", 'r', encoding='utf-8') as f:
        google = json.load(f)
    compare(youdao)