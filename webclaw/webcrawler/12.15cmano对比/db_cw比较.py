#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: db_cw比较.py    
@Time: 2021/12/15 9:29 
"""
import json

if __name__ == '__main__':
    with open('cmano_cw/submarine_cw全部519.json', 'r', encoding='utf-8') as f:
        file1 = json.load(f)
    with open('cmano_db/submarine全部646.json', 'r', encoding='utf-8') as f:
        file2 = json.load(f)
    count = 1
    countrycount = 1
    con = {}
    data = []
    typecount = 1
    for i in range(len(file1)):
        for j in range(len(file2)):

            if file1[i]['title'] == file2[j]['title']:
                con["title"] = file1[i]['title']
                if file1[i]['Country/Type'] == file2[j]['Country/Type']:
                    con["Country/Type"] = '相同'
                    countrycount += 1

                for k in file1[i]['General data']:
                    print(k.values(k))
                    for l in file2[j]['General data']:
                        if k.keys() == l.keys():
                            print(k.keys())
                            if k.values() == l.values():
                                typecount += 1
                con["General data"] = '有'+ str(typecount) +'个相同属性'

                count += 1
            data.append(con)

    #
    # with open('cmano_db_cw/submarine重复数据.json', 'w', encoding='utf-8') as f:
    #     json.dump(con, f, indent=4, ensure_ascii=False)
    # print(json.dumps(data, indent=4, ensure_ascii=False))
    # print(count, countrycount)
