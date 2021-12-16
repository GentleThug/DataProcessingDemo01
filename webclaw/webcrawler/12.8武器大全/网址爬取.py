from bs4 import BeautifulSoup
import requests
import json
import random
import socket


def pachong(num):
    global response
    url = 'https://wuqi.supfree.net/ufo.asp?classify=' + \
        'explosive' + '&page=' + str(num)
    try:
        response = requests.get(url)
        response.encoding = 'UTF-8'
    except IndexError as e:
        return str(num) + '网页为空'
    except socket.timeout as e:
        response.close()
        return str(num) + '网页超时'
    except requests.HTTPError as e:
        return str(num) + '爬取错误'
    result = []
    soup = BeautifulSoup(response.text, 'html.parser')
    a_href = soup.find_all(class_="row")
    # tables = soup.find_all("table")
    # pageheader = soup.find_all(class_="page-header")
    # sign = 1
    for a in a_href:
        for i in a.find_all("a"):
            # title = i.find("h4").text
            href = i['href']
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
    chushi = 32
    tiaoshu = 1
    for i in range(chushi):
        # time.sleep(random.random()*0.3)
        # time.sleep(0.2)
        result = pachong(chushi)

        if result:
            print(str(chushi) + '已查找' + str(tiaoshu) + '页')
            all += result
            chushi -= 1
            tiaoshu += 1

            # if tiaoshu % 100 == 0:
            #     with open('网页/wuqi' + str(tiaoshu) + '.json', 'w', encoding='utf-8') as f:
            #         json.dump(all, f, indent=4, ensure_ascii=False)
            #     # print('已写入，等待几十秒继续')
            #     # time.sleep(random.random() * 30)
            # # 结束条件
            if chushi < 0:
                break
        else:
            chushi -= 1
            print(result)

    with open('网页/' + 'explosive' + '.json', 'w', encoding='utf-8') as f:
        json.dump(all, f, indent=4, ensure_ascii=False)
