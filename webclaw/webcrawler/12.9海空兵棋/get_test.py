from bs4 import BeautifulSoup
import requests
import json
import random
import re


def pachong(src_type, num):
    global response
    headers = get_headers()
    url = 'http://hkbq.imis.ltd:8888/webroot/decision/view/report?viewlet=%252FAdvanced%252F' + str(src_type) + '_detail-hkbq.cpt&__parameters__=%257B%2522__pi__%2522%253Atrue%252C%2522ID%2522%253A' + str(num)
    try:
        response = requests.get(url, headers=headers)
        response.encoding = 'UTF-8'
    except:
        return str(num) + '爬取错误'
    result = []
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    a_href = url
    id = soup.find_all(id=re.search("E4-\d-\d{3}",soup.text))
    print(id)

    for i in id:
        if len(i.text) > 0:
            href = a_href['href']
            result.append(href)

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
    chushi = 680
    src_type = 'Submarine'
    tiaoshu = 1

    result = pachong(src_type, chushi)
    print(json.dumps(result, indent=4, ensure_ascii=False))
    # for i in range(chushi):
    #     # time.sleep(random.random()*0.3)
    #     # time.sleep(0.2)
    #     result = pachong(src_type, chushi)
    #
    #     if result:
    #         print(str(chushi) + '已查找' + str(tiaoshu) + '页')
    #         all += result
    #         chushi -= 1
    #         tiaoshu += 1
    #
    #         # if tiaoshu % 100 == 0:
    #         #     with open('网页/wuqi' + str(tiaoshu) + '.json', 'w', encoding='utf-8') as f:
    #         #         json.dump(all, f, indent=4, ensure_ascii=False)
    #         #     # print('已写入，等待几十秒继续')
    #         #     # time.sleep(random.random() * 30)
    #         # # 结束条件
    #         if chushi < 0:
    #             break
    #     else:
    #         chushi -= 1
    #         print(result)
    #
    # with open('网页/' + 'explosive' + '.json', 'w', encoding='utf-8') as f:
    #     json.dump(all, f, indent=4, ensure_ascii=False)
