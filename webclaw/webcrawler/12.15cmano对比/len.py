#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: len.py    
@Time: 2021/12/14 16:34 
"""
import json
if __name__ == '__main__':
    with open('cmano_db/aircraft全部5231.json', 'r', encoding='utf-8') as f:
        data1 = json.load(f)
    with open('cmano_db/facility全部3314.json', 'r', encoding='utf-8') as f:
        data2 = json.load(f)
    with open('cmano_db/sensor全部6208.json', 'r', encoding='utf-8') as f:
        data3 = json.load(f)
    with open('cmano_db/ship全部3382.json', 'r', encoding='utf-8') as f:
        data4 = json.load(f)
    with open('cmano_db/submarine全部646.json', 'r', encoding='utf-8') as f:
        data5 = json.load(f)
    with open('cmano_db/weapon全部3715.json', 'r', encoding='utf-8') as f:
        data6 = json.load(f)
    print(len(data1)+len(data2)+len(data3)+len(data4)+len(data5)+len(data6))
    print(len(data1))
    print(len(data2))
    print(len(data3))
    print(len(data4))
    print(len(data5))
    print(len(data6))

