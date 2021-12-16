#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: test.py    
@Time: 2021/12/16 15:20 
"""
import json

if __name__ == '__main__':
    with open('cmano_cw/submarine_cw全部519.json', 'r', encoding='utf-8') as f:
        file1 = json.load(f)
    with open('cmano_db/submarine全部646.json', 'r', encoding='utf-8') as f:
        file2 = json.load(f)
    count = 0
    data = []
    con = {}
    # 冷战
    for i in file1:
        # DB
        for j in file2:
            print(i['General data'][0])
            break