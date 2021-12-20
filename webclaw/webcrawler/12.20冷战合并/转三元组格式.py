#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 转三元组格式.py    
@Time: 2021/12/20 15:16 
"""
import json
import os


if __name__ == '__main__':
    base_dir = '../12.17统计/merge'
    base_dir_cw = '../12.16冷战camno/cmano_cw'
    base_dir_db = '../12.16冷战camno/cmano_db'
    lst_res = []
    for file in os.listdir(base_dir):
        # print(base_dir,file)
        with open(os.path.join(base_dir, file), encoding='utf8') as fr:
            lst_json = json.load(fr)
            lst_res.extend(lst_json)
    class_name = []
    for dic in lst_res:
        data = dic['General data']
        for d in data:
            for i in list(d.keys()):
                class_name.append(i)
    print(len(list(set(class_name))))
    print(set(class_name))
