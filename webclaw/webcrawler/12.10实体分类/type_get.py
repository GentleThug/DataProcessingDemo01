#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: type_get.py    
@Time: 2021/12/10 10:04 
"""
import re

from bs4 import BeautifulSoup
import requests
import json


def cdiv_get(soup):
    global p_type
    cdiv = soup.find(class_="cdiv")
    # 进入P标签
    for t in cdiv.find_all('p'):
        # 列表
        if t is not cdiv.find_all('p')[0]:
            if t is not cdiv.find_all('p')[2]:
                # 去掉：
                p_type = t.find("strong").text.split('：')
                content = {}
                for i in t.find_all('a'):
                    href = i['href']
                    content[i.text] = href
                    result[p_type[0]] = content
    return result


if __name__ == '__main__':
    # with open('武器/网页/aircraft.json', 'r', encoding='utf-8') as f:
    #     data = json.load(f)
    # for d in data:
    # 8_antitank  4_tanks md902
    data = [
        "https://wuqi.supfree.net/ufo.asp?classify=aircraft",
        "https://wuqi.supfree.net/ufo.asp?classify=artillery",
        "https://wuqi.supfree.net/ufo.asp?classify=explosive",
        "https://wuqi.supfree.net/ufo.asp?classify=guns",
        "https://wuqi.supfree.net/ufo.asp?classify=missile",
        "https://wuqi.supfree.net/ufo.asp?classify=spaceship",
        "https://wuqi.supfree.net/ufo.asp?classify=tank",
        "https://wuqi.supfree.net/ufo.asp?classify=warship",
    ]
    all = []
    for url in data:
        response = requests.get(url)
        response.encoding = 'UTF-8'
        result = {}
        content = {}
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup)

        all.append(cdiv_get(soup))
    #
    with open('type/type_web.json', 'w', encoding='utf-8') as f:
        json.dump(all, f, indent=4, ensure_ascii=False)
    # print(json.dumps(all, indent=4, ensure_ascii=False))
