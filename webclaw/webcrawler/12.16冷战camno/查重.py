#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 查重.py    
@Time: 2021/12/16 19:41 
"""
import json
if __name__ == '__main__':
    with open('冷战cmano对比/aircraft对比数据1201.json', 'r', encoding='utf-8') as f:
        file1 = json.load(f)

    for i in file1:
        count = 0
        for j in file1:
            if i['title'] == j['title']:
                if i['Country/Type'] == j['Country/Type']:
                    if i['different_data'] == j['different_data']:
                        count += 1
                        if count > 1:
                            print(i['title'],count)