"""
#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:LJY
"""

from bs4 import BeautifulSoup
import requests
import json
import random


def pachong(url):
    headers = get_headers()
    response = requests.get(url, headers=headers)
    response.encoding = 'UTF-8'
    result = {}
    content = {}
    soup = BeautifulSoup(response.text, 'html.parser')
    # 按照class查找
    cdiv = soup.find_all(class_="cdiv")
    # 按照css标签查找
    pageheader = soup.find_all("h2")

    for t in pageheader:
        try:
            title = t.text
        except IndexError as e:
            print(result)
        result["title"] = title
        result["url"] = url
    # 当前网页中需要跳过cdiv个数
    cdiv_num = 1  # 默认一个
    # cdiv当前位置
    cdiv_local = 1
    # cdiv开始查找次数
    cdiv_start = 1

    for t in cdiv:
        # 如果有图片cdiv，跳过次数加一
        for i in t.find_all(class_="img-responsive"):
            cdiv_num += 1
        # 跳过判断
        if cdiv_local <= cdiv_num:
            cdiv_local += 1
        else:

            # 输出国家信息
            for i in t.find_all("small"):
                if len(i.text) is not 1:
                    list1 = i.text.split('：')
                    result[list1[0]] = list1[1]
            # 首个爬取cdiv获取标题及文本
            if cdiv_start == 1:
                # title = t.find("h3").text
                content["text"] = t.text
                cdiv_start += 1
            # 技术数据cdiv
            elif cdiv_start == 2:
                title = t.find("h4").text
                content[title] = []
                for i in t.find_all("li"):
                    if i.text.find('：') > 0 and i.text.find('（1）') < 0:
                        list1 = i.text.split('：')
                        dic = {
                            list1[0]: list1[1]
                        }
                        content[title].append(dic)
                    else:
                        # 父节点的上兄弟节点
                        str_title = i.parent.previous_sibling.text
                        # content[title].append(dic)
                        content[str_title] = i.text
                    cdiv_start += 1
            # 后续cdiv文本
            else:
                title = t.find("h4").text
                content[title] = t.text
    result["content"] = content
    return result


# 模拟网页访问头
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
    with open('网页/tank.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    tiaoshu = 1
    all = []
    for d in data:
        print(d + '已查找' + str(tiaoshu) + '条')
        all.append(pachong(d))
        tiaoshu += 1
        # if tiaoshu % 500 == 0:
        #     with open('武器类别/tank' + str(tiaoshu) + '.json', 'w', encoding='utf-8') as f:
        #         json.dump(all, f, indent=4, ensure_ascii=False)

    with open('武器类别/tank' + str(len(all)) + '.json', 'w', encoding='utf-8') as f:
        json.dump(all, f, indent=4, ensure_ascii=False)
