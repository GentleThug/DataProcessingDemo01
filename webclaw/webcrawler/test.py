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
import socket
import time
import urllib.request
import urllib.parse

from lxml import etree


def pachong(num):
    global response
    url = 'http://cmano-db.com/weapon/' + str(num) + '/'
    headers = get_headers()
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

    # 使用 xpath 匹配数据，得到匹配字符串列表
    # time = html.xpath('/html/body/div/div[1]/div[3]/table/tbody/tr[3]/td/div/table/tbody/tr[11]/td/div[2]/span//text()')[0]
    # author = ta_list[2].strip()
    try:
        req = urllib.request.Request(url=url, headers=headers, method='GET')
        response = urllib.request.urlopen(req, timeout=4)
        text = response.read()
        html = etree.HTML(text)
        title = html.xpath('/html/body/div[2]/div[2]/div[1]/div/h3//text()')[0]
        for i in range(1, 10):
            text_list = html.xpath('/html/body/div[2]/div[2]/div[2]/table[' + str(i) + ']//text()')

            if len(text_list[0]) == 0:
                pass
            else:
                text_list[i - 1] = tihuan(text_list)

            print(text_list[i - 1])
            content = ''.join(text_list[i - 1])


    except IndexError as e:
        return str(num) + '网页为空'
    except socket.timeout as e:
        response.close()
        return str(num) + '网页超时'
    except urllib.request.HTTPError as e:
        return str(num) + '爬取错误'

    # 使用 xpath 匹配数据，得到匹配字符串列表
    # time = html.xpath('/html/body/div/div[1]/div[3]/table/tbody/tr[3]/td/div/table/tbody/tr[11]/td/div[2]/span//text()')[0]
    # author = ta_list[2].strip()



    # ta_list = html.xpath('//div[@class="Padding10 TxtCenter Gray BorderTopDot Top10"]//text()')[0] \
    #     .replace("发布时间", "").replace(" ", "").replace("作者", "").replace("浏览次数", "").split("：")
    # pipei = re.search("[\d]{4}-[\d]{1,2}-[\d]{1,2}", time, flags=0)
    # if pipei:
    #     time = time[pipei.span()[0]:pipei.span()[1]]

    p = {
        "title": title,
        # "time": time,
        # "author": author,
        "url": url,
        "content": content
    }
    return p


def tihuan(text_list):
    text_list = str(text_list).replace('\\t', '')
    text_list = str(text_list).replace('\\n', '')
    text_list = str(text_list).replace('\\', '')
    text_list = str(text_list).replace('  ', '')
    # 过滤数据，去掉空白 将字符串列表连成字符串并返回
    return text_list


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
    # 初始网址
    chushi = 1000
    # chushi = 6488
    # chushi = 6109
    tiaoshu = 1
    for i in range(chushi):
        # time.sleep(random.random()*0.3)
        # time.sleep(0.2)
        p = pachong(chushi)

        if isinstance(p, dict):
            print(str(chushi) + '已查找' + str(tiaoshu) + '条')
            all.append(p)
            chushi -= 1
            tiaoshu += 1

            if tiaoshu % 1000 == 0:
                with open('12.6军事数据/sensor/sensor' + str(tiaoshu) + '.json', 'w', encoding='utf-8') as f:
                    json.dump(all, f, indent=4, ensure_ascii=False)
                # print('已写入，等待几十秒继续')
                # time.sleep(random.random() * 30)
            # 结束条件
            if chushi < 3487:
                break
        else:
            chushi -= 1
            print(p)

    with open('12.6军事数据/sensor/sensor' + '断点' + str(tiaoshu) + '.json', 'w', encoding='utf-8') as f:
        json.dump(all, f, indent=4, ensure_ascii=False)
