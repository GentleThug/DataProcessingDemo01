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


def page_get(url):
    response = requests.get(url)
    response.encoding = 'UTF-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        page_text = soup.find(class_="ulink")
        page_num = re.search("(\d{1,3})页", page_text.text).group()
        page_num = re.search("\d{1,3}", page_num).group()
    except:
        return
    return page_num


def type_get(url, page, class_name, attr):
    result = []
    content = {}
    if page is None:
        print('*************************************************************************')
    if page is not None:
        page = int(page)
        for i in range(page):
            page_url = url + '&page=' + str(page)
            # print(page)
            response = requests.get(page_url)
            response.encoding = 'UTF-8'
            soup = BeautifulSoup(response.text, 'html.parser')
            a_title = soup.find_all(class_="row")

            for a in a_title:
                for t in a.find_all("a"):
                    title = t['title']
                    content["title"] = title
                    content[class_name] = attr
                    z = {}
                    for con in content.keys():
                        z[con] = content[con]
                    result.append(z)
            page -= 1
            if page == 0:
                break

    print("------")
    return result


if __name__ == '__main__':
    with open('type/type_web.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    result = []
    # 进入data   层级关系：one two
    for i in data:
        for one, two in i.items():
            print(one)
            # for two_key in two.keys():
            #     print(two_key)
            for two_key, two_url in two.items():
                print(two_key)
                # 属性网址
                two_url = 'https://wuqi.supfree.net/' + str(two_url)
                page = page_get(two_url)
                result.append(type_get(two_url, page, one, two_key))
    with open('type/type_relations.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
    # print(json.dumps(resule, indent=4, ensure_ascii=False))
