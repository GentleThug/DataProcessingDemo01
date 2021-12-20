#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 统计.py    
@Time: 2021/12/17 11:30 
"""
import json

if __name__ == '__main__':
    with open('res_Weapon_data_qvchong_12.14.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    name1 = 1
    dic = {
        "武器装备": 0,
        "结构特点": 0,
        "使用情况": 0,
        "型号演变": 0
    }
    num = 0
    for i in file:
        for j, k in i.items():
            count = 0
            for l in k:
                if l in dic:
                    count += 1
            if count > 0:
                num += 1

    print(num)

