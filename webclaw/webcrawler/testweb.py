# -*- coding: UTF-8 -*-
"""
describe:
@author: LSW66
@file: test2.py
@time: 2021/11/27/9:19
"""
import json
import random
import re
import time
import urllib.request
import urllib.parse

from lxml import etree


def pachong(num):
    url = 'https://www.chinabidding.com/bidDetail/' + str(num) + '.html'
    headers = get_headers()
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers, method='GET')

    try:
        urllib.request.urlopen(req)
    except urllib.request.URLError as e:
        return str(num) + ' 这个网页404了'

    response = urllib.request.urlopen(req)
    text = response.read().decode('utf-8')
    html = etree.HTML(text)

    # 使用 xpath 匹配数据，得到匹配字符串列表
    title = html.xpath('/html/body/div/div[4]/div/div[2]/div[1]/div//text()')[0]
    time = html.xpath('/html/body/div/div[4]/div/div[2]/div[1]/div/p/span//text()')[0].replace(" ", "")
    # author = ta_list[2].strip()
    text_list = html.xpath('/html/body/div/div[4]/div/div[2]/div[1]/div/div[2]//text()')
    # ta_list = html.xpath('//div[@class="Padding10 TxtCenter Gray BorderTopDot Top10"]//text()')[0] \
    #     .replace("发布时间", "").replace(" ", "").replace("作者", "").replace("浏览次数", "").split("：")

    pipei = re.search("[\d]{4}-[\d]{1,2}-[\d]{1,2}", time, flags=0)
    if pipei:
        time = time[pipei.span()[0]:pipei.span()[1]]

    # 过滤数据，去掉空白 将字符串列表连成字符串并返回
    content = ''.join([item.strip('\n') for item in text_list])

    p = {
        "title": title,
        "time": time,
        # "author": author,
        "url": url,
        "content": content
    }
    return p

def get_headers():
    pc_agent = [
        # "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        # "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36",
    ]

    if pc_agent:  # 随机选择一个
        agent = random.choice(pc_agent)

    headers = {
        'User-Agent': agent,
    }
    return headers


if __name__ == '__main__':
    all = []
    #初始网址
    chushi = 251044111
    for i in range(chushi):
        time.sleep(random.random()*2)
        p = pachong(chushi)

        if isinstance(p, dict):
            print(str(chushi) + '已查找')
            all.append(p)
            chushi -= 1

            if chushi % 500 == 0:
                with open('12.6军事数据/12.6军事数据' + str(len(all)) + '.json', 'w', encoding='utf-8') as f:
                    json.dump(all, f, indent=4, ensure_ascii=False)
            #结束条件
            if chushi < 2:
                break
        else:
            chushi -= 1
            print(p)

    with open('12.6军事数据/12.6军事数据' + str(len(all)) + '.json', 'w', encoding='utf-8') as f:
        json.dump(all, f, indent=4, ensure_ascii=False)


