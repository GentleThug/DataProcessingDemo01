from bs4 import BeautifulSoup
import requests
import json



if __name__ == '__main__':
    url = 'https://cmano-db.com/facility/3412/'
    response = requests.get(url)
    result = {}

    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all("table")
    pageheader = soup.find_all(class_ ="page-header")
    sign = 1
    for t in pageheader:
        try:
            title = t.find("h3").text
        except IndexError as e:
            print("网页为空")
        result["title"] = title
        print(result)
    for t in tables:
        try:
            title = t.find("th").text
            print(title)
        except:
            title = "Properties:"
        result[title] = []
        if sign == 1:
            for i in t.find_all("td"):
                print(len(i.text))
                if len(i.text) > 1:
                    list1 = i.text.split(':')
                    print(list1)
                    dic = {
                        list1[0]: list1[1]
                    }
                    result[title].append(dic)
            sign += 1
        else:
            for i in t.find_all("td"):
                result[title].append(i.text)




    print(json.dumps(result,indent=4,ensure_ascii=False))
