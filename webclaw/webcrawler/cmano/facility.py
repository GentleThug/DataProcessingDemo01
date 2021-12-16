from bs4 import BeautifulSoup
import requests
import json
import random
import socket

from tqdm import tqdm


def pachong(num):
    global response
    url = 'http://cmano-db.com/facility/' + str(num) + '/'
    headers = get_headers()
    try:
        response = requests.get(url, headers=headers, timeout=5)
    except:
        return str(num) + '爬取错误'
    result = {}
    content = {}
    soup = BeautifulSoup(response.text, 'html.parser')
    pageheader = soup.find_all(class_="page-header")
    country_type = soup.find_all(class_="breadcrumb")
    tables = soup.find_all("table")

    sign = 1
    for t in pageheader:
        try:
            title = t.find("h3").text
        except IndexError as e:
            return str(num) + '网页为空'
        result["title"] = title
        result["url"] = url

    for t in country_type:
        # 所有li列表的第二个
        country_type_res = t.find_all("li")[1].text
        result["Country/Type"] = country_type_res

    for t in tables:
        try:
            title = t.find("th").text
        except:
            title = "Properties:"
        result[title] = []
        if sign == 1:
            for i in t.find_all("td"):
                if len(i.text) > 1:
                    list1 = i.text.split(':')
                    content[list1[0]] = list1[1]
            result[title].append(content)
            sign += 1
        else:
            for i in t.find_all("td"):
                result[title].append(i.text)

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
    # 初始网址
    chushi = 3413
    tiaoshu = 1
    for i in tqdm(range(chushi)):
        # time.sleep(random.random()*0.3)
        # time.sleep(0.2)
        result = pachong(chushi)

        if result:
            # print(str(chushi) + '已查找' + str(tiaoshu) + '条')

            all.append(result)
            chushi -= 1
            tiaoshu += 1

            # if tiaoshu % 1000 == 0:
            #     with open('12.6军事数据/facility/facility' + str(tiaoshu) + '.json', 'w', encoding='utf-8') as f:
            #         json.dump(all, f, indent=4, ensure_ascii=False)
                # print('已写入，等待几十秒继续')
                # time.sleep(random.random() * 30)
            # 结束条件
            if chushi < 0:
                break
        else:
            chushi -= 1
            print(result)

    with open('12.9/facility' + '全部' + str(tiaoshu) + '.json', 'w', encoding='utf-8') as f:
        json.dump(all, f, indent=4, ensure_ascii=False)
