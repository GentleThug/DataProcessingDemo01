#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 导出title.py    
@Time: 2021/12/22 9:30 
"""
import json
import os
from tqdm import tqdm

if __name__ == '__main__':
    # 待转换文件目录路径
    base_dir = '../../../data/cmano/merge'
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
        for keyname, valuename in data_block.items():
            if keyname == "title":
                count += 1
                content[valuename] = count
                result.append(valuename)
    content = list(content)
    content.sort()
    with open('cmano_tilte去重（' + str(len(content)) + '）.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=4, ensure_ascii=False)
    with open('cmano_tilte（' + str(len(result)) + '）.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
    # print(json.dumps(content, indent=4, ensure_ascii=False))
    # print(len(content))