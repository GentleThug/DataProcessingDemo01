#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 筛选.py    
@Time: 2021/12/15 14:08 
"""
import json
import re

if __name__ == '__main__':
    with open('武器大全/武器大全_quchong.json', 'r', encoding='utf-8') as f:
        file1 = json.load(f)
    # with open('关键数据/F-15.json', 'r', encoding='utf-8') as f:
    #     file1 = json.load(f)
    result = []
    count = 0
    tiaojian = "F-15"
    for i in range(len(file1)):
        try:
            title = re.search(tiaojian, file1[i]['title'])
        except:
            print(file1[i], "出错了************")

        if title:
            count += 1
            print(file1[i]['title'])
            result.append(file1[i])
        # if title:
        #     print(file1[i]['title'])

    print(count)

    with open('武器大全/' + tiaojian + '.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
    # with open('关键数据/F-15.json', 'w', encoding='utf-8') as f:
    #     json.dump(result, f, indent=4, ensure_ascii=False)
    # print(json.dumps(result, indent=4, ensure_ascii=False))
