#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 去重.py    
@Time: 2021/12/11 10:34 
"""
import json


def uniqueArray(array, key):
    result = [array[0]]
    for i in range(len(array)):
        item = array[i]
        # print(item)
        repeat = False
        i += 1
        for j in range(len(result)):
            if item[key] == result[j][key]:
                repeat = True
                break
            j += 1


        if not repeat:
            result.append(item)

    return result


if __name__ == '__main__':
    with open('武器大全.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    con = []
    for i in range(len(data)):
        print(i)
        arr = data[i]
        result = uniqueArray(data[i], "title")
        print(result)
        con.append(result)

    with open('武器大全_原数据去重.json', 'w', encoding='utf-8') as f:
        json.dump(con, f, indent=4, ensure_ascii=False)
    # print(json.dumps(con, indent=4, ensure_ascii=False))
