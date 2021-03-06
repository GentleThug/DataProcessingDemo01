#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 转三元组格式.py    
@Time: 2021/12/20 15:16 
"""
import json
import os

from tqdm import tqdm


# 取出General data的属性
def remove_General_data(data_block):
    result = {}
    for keyname, valuename in data_block.items():
        if keyname == 'General data':
            for i_key, i_value in valuename[0].items():
                result[i_key] = i_value
        else:
            result[keyname] = valuename
    return result


# 转换格式块
def transform_block(return_block):
    # 索引
    indexes = {}
    # 索引内容
    index_content = {}

    # 来源
    source = return_block['url']
    for keyname, valuename in return_block.items():
        # 键值内容
        content = {}

        # url跳过
        if keyname == 'url':
            continue
        elif len(valuename) < 1:
            continue
        # 四类有列表值的
        elif keyname == "Sensors / EW" or keyname == "Weapons / Loadouts" or keyname == "Properties" or keyname == "Targets" or keyname == "Weapons":
            list_content = []
            content = {}
            # 列表内容
            for i in valuename:
                content["value"] = i
                content["source"] = source
                z = {}
                for i in content:
                    z[i] = content[i]
                list_content.append(z)
                index_content[keyname] = list_content
        else:
            content["value"] = valuename
            content["source"] = source
            index_content[keyname] = content
            # print(index_content)
    indexes[source] = index_content
    return indexes

# 调整写入json格式
def json_format(base_dir, result):
    if base_dir == 'data/原版':
        filename = "原版转格式(v1.0)"
    # if base_dir == 'data/冷战':
        filename = "冷战转格式(v1.0)"

    print(filename)
if __name__ == '__main__':
    # 文件目录
    base_dir = '../../../data/cmano/merge'
    # base_dir = '../12.20冷战合并/test'
    # 文件列表
    lst_res = []
    result = []
    for file in os.listdir(base_dir):
        with open(os.path.join(base_dir, file), encoding='utf8') as fr:
            lst_json = json.load(fr)
            lst_res.extend(lst_json)

    # 读取数据块
    for data_block in tqdm(lst_res):
        return_block = remove_General_data(data_block)
        i = transform_block(return_block)
        result.append(i)
    with open('cmano转格式.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
