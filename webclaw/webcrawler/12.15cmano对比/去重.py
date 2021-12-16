#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 去重.py    
@Time: 2021/12/11 10:34 
"""
import json


def uniqueArray(array, key):
    count = 0
    result = [array[0]]
    for i in range(len(array)):
        item = array[i]
        # print(item)
        repeat = False
        i += 1
        for j in range(len(result)):
            if item[key] == result[j][key]:
                print(item[key])
                count += 1
                repeat = True
                break
            j += 1


        if not repeat:
            result.append(item)
    print(count)
    return result


if __name__ == '__main__':
    with open('cmano_db/facility全部3314.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    result = uniqueArray(data, "title")


    with open('cmano_去重/facility_db 去重' + str(len(result)) + '.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
    # print(json.dumps(con, indent=4, ensure_ascii=False))
