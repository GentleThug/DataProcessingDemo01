#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: len.py    
@Time: 2021/12/21 10:55 
"""

import json
import os

if __name__ == '__main__':
    # 文件目录
    base_dir = '原数据/冷战/aircraft_cw全部3836.json'
    # base_dir = '../12.20冷战合并/test'
    # 文件列表
    lst_res = []
    result = []
    with open(base_dir, 'r', encoding='utf-8') as f:
        lst_res = json.load(f)
    # for file in os.listdir(base_dir):
    #     with open(os.path.join(base_dir, file), encoding='utf8') as fr:
    #         lst_json = json.load(fr)
    #         lst_res.extend(lst_json)
    print(len(lst_res))