#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 武器title.py    
@Time: 2021/12/22 14:54 
"""
import json
import os
from tqdm import tqdm

if __name__ == '__main__':
    # 待转换文件目录路径
    base_dir = '武器'
    # 文件列表
    lst_res = []
    # 结果列表
    result = []
    content = {}
    count = 0
    for file in os.listdir(base_dir):
        with open(os.path.join(base_dir, file), encoding='utf8') as fr:
            lst_json = json.load(fr)
            lst_res.extend(lst_json)

    for data_block in tqdm(lst_res):
        main_key = data_block['content'].get('技术数据')[0].get('名称').replace("\t", "").strip()
        count += 1
        content[main_key] = count

    content = list(content)
    content.sort()
    with open('武器_tilte去重（' + str(len(content)) + '）.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=4, ensure_ascii=False)

    # print(json.dumps(content, indent=4, ensure_ascii=False))
    # print(len(content))