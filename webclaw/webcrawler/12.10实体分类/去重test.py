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
    print(result)
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
    with open('type/type_relations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    con = []
    for i in range(len(data)):
        print(i)
        arr = data[i]
        # 进入data   层级关系：one two
        result = uniqueArray(data[i], "title")
        print(result)
        con.append(result)

    # with open('type/type_relations_quchong.json', 'w', encoding='utf-8') as f:
    #     json.dump(con, f, indent=4, ensure_ascii=False)
    # print(json.dumps(con, indent=4, ensure_ascii=False))
