#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: test.py    
@Time: 2021/12/17 14:21 
"""
import json
import os
import pandas as pd
import numpy as np

def base_file(base_dir):
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
    if base_dir == "../12.16冷战camno/cmano_cw":
        cw = list(set(class_name))
        return cw
    if base_dir == "../12.16冷战camno/cmano_db":
        db = list(set(class_name))
        return db


if __name__ == '__main__':
    base_dir = 'merge'
    base_dir_cw = '../12.16冷战camno/cmano_cw'
    base_dir_db = '../12.16冷战camno/cmano_db'
    base_file(base_dir)
    cw = base_file(base_dir_cw)
    db = base_file(base_dir_db)
    for i in db:
        if i not in cw:
            print(i)




    # for file in os.listdir(base_dir):
    #     print(file)
    #     with open(os.path.join(base_dir, file), encoding='utf8') as fr:
    #         lst_json = json.load(fr)
    #         lst_res.extend(lst_json)
    # class_name = []
    # for dic in lst_res:
    #     data = dic['General data']
    #     for d in data:
    #         for i in list(d.keys()):
    #             class_name.append(i)
    # print(len(list(set(class_name))))
    # print(list(set(class_name)))
