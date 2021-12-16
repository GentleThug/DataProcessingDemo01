#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 合并.py    
@Time: 2021/12/11 11:13 
"""
import json


def uniqueArray(array):
    result = array[0]
    data = []
    for i in range(len(result)):
        content = {}
        print(i)
        title_name = result[i]['title']
        # 遍历，进行比对
        for j in range(len(result)):
            j_name = result[j]['title']
            # 如果title相等
            if j_name == title_name:
                # 将title相等的字典元素都放在content中
                content['title'] = result[i]['title']
                for k, h in result[j].items():
                    content[k] = h
            if j == len(result):
                break
        z = {}
        for n in content.keys():
            z[n] = content[n]
        data.append(z)
    return data


if __name__ == '__main__':
    with open('武器大全.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    con = []
    # data = [
    # {
    #     "title": "Saab-35龙",
    #     "分类：": "战斗机"
    # },
    # {
    #     "title": "Saab-35龙",
    #     "年代：": "二战后至冷战期间"
    # },
    # {
    #     "title": "X-35",
    #     "分类：": "战斗机"
    # },
    # {
    #     "title": "X-35",
    #     "年代：": "冷战后至今"
    # },
    # {
    #     "title": "X-35",
    #     "123：": "二战后至冷战期间"
    # },
    # ]
    result = uniqueArray(data)
    con.append(result)

    with open('武器大全.json', 'w', encoding='utf-8') as f:
        json.dump(con, f, indent=4, ensure_ascii=False)
    # print(json.dumps(con, indent=4, ensure_ascii=False))
