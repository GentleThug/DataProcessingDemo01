#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 补充sensor_weapon.py
@Time: 2021/12/31 10:14 
"""
import time

from bs4 import BeautifulSoup
import requests
import json
import random
from tqdm import tqdm


# 爬虫函数
def pachong(num):
    global response
    url = 'http://cmano-db.com/' + str(num) + '/'
    # url= 'http://cmano-db.com/weapon/3872/'
    # 获取随机访问头
    headers = get_headers()
    # 尝试3次
    try:
        response = requests.get(url, headers=headers, timeout=5)
    except:
        time.sleep(0.2)
        try:
            response = requests.get(url, headers=headers, timeout=5)
        except:
            time.sleep(0.2)
            try:
                response = requests.get(url, headers=headers, timeout=5)
            except:
                print("\n", url + '爬取错误')
                return url + '爬取错误'
    result = {}
    soup = BeautifulSoup(response.text, 'html.parser')
    pageheader = soup.find_all(class_="page-header")
    country_type = soup.find_all(class_="breadcrumb")
    tables = soup.find_all("table")

    # 获取标题
    for t in pageheader:
        title = t.find("h3").text
        if len(title) < 1:
            continue
        result["title"] = title
        result["url"] = url
    # 获取country/type
    for t in country_type:
        # 所有li列表的第二个
        country_type_res = t.find_all("li")[1].text
        result["Country/Type"] = country_type_res
    # table框架
    for t in tables:
        try:
            # 尝试获取th
            keys = t.find("th").text
            title = keys.replace(":", "")
        except:
            for h in t.find_all("td"):
                if len(h.text) > 1:
                    g = h.text.split(':')
                    title = g[0]
        if title == "General data":
            pass
        else:
            result[title] = []
        if title == "General data":
            for i in t.find_all("td"):
                if len(i.text) > 1:
                    list1 = i.text.split(':')
                    result[list1[0].strip()] = list1[1].strip()

        elif title == "Sensors / EW" or title == "Weapons" or title == "Weapons / Loadouts":
            content = {}
            for i in t.find_all("td"):
                try:
                    for keys in i.find("b"):
                        href = keys['href']
                        content[keys.text] = 'http://cmano-db.com/' + href
                except:
                    if len(i.text) > 1:
                        list1 = i.text.split(' - ')
                        content[list1[0]] = list1[1]
            result[title].append(content)

        else:
            for i in t.find_all("td"):
                if len(i.text.split(':')) > 1:
                    result[title].append((i.text.split(':')[1]).strip())
                else:
                    result[title].append(i.text.strip())
        #         result[title].append(i.text)
        # result[title] = []
    return result


def get_headers():
    global agent
    pc_agent = [
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    ]

    if pc_agent:  # 随机选择一个
        agent = random.choice(pc_agent)

    headers = {
        'User-Agent': agent,
    }
    return headers


if __name__ == '__main__':
    all = []
    chushi = 3413
    web_url = "facility"

    tiaoshu = 1
    for i in tqdm(range(chushi)):
        # time.sleep(random.random()*0.3)
        time.sleep(0.2)
        j = pachong(web_url + '/' + str(chushi))
        if len(j) < 1:
            # print('http://cmano-db.com/' + '/' + web_url + str(chushi) + '/', "网页为空")
            pass
        else:
            all.append(j)
        chushi -= 1
        tiaoshu += 1
        if chushi < 0:
            break
    with open(web_url + str(len(all)) + '.json', 'w', encoding='utf-8') as f:
        json.dump(all, f, indent=4, ensure_ascii=False)

    # j = pachong(web_url + '/' + str(chushi))
    # if len(j) < 1:
    #     # print('http://cmano-db.com/' + '/' + web_url + str(chushi) + '/', "网页为空")
    #     pass
    # else:
    #     all.append(j)
    # print(json.dumps(all, indent=4, ensure_ascii=False))
