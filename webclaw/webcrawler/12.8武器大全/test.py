import re

from bs4 import BeautifulSoup
import requests
import json


def cdiv_get(soup):
    pageheader = soup.find_all("h2")
    cdiv = soup.find_all(class_="cdiv")

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
                    str_title = i.parent.previous_sibling.text
                    if str_title == "武器装备" or str_title == "有效载荷" or str_title == "结构尺寸":
                        content[str_title] = i.text

                    else:
                        list1 = i.text.split('：')
                        dic = {
                            list1[0]: list1[1]
                        }
                        content[title].append(dic)
                    cdiv_start += 1
            else:
                title = t.find("h4").text
                content[title] = t.text
    result["content"] = content
    return result


if __name__ == '__main__':
    # with open('武器/网页/aircraft.json', 'r', encoding='utf-8') as f:
    #     data = json.load(f)
    # for d in data:
    # 8_antitank  4_tanks md902
    url = "https://wuqi.supfree.net/weapon.asp?id=changzheng_5"
    # url = "https://wuqi.supfree.net/weapon.asp?id=bell_212"
    response = requests.get(url)
    response.encoding = 'UTF-8'
    result = {}
    content = {}
    soup = BeautifulSoup(response.text, 'html.parser')

    cdiv_get(soup)

    print(json.dumps(result, indent=4, ensure_ascii=False))
