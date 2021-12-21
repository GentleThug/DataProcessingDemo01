#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 转格式.py
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
    """
    json结构：
    [
        indexes{
            index_content{
                content
                },
            index_content[
                {content},
                {content}
            ]
        }
    ]

    变量值结构：
    [
        source：{
            keyname：{"value": "valuename", "source": "source"},
            keyname：[
                {"value": "valuename", "source": "source"},
                {"value": "valuename", "source": "source"}
            ]
        }
    ]
    """
    # 索引字典
    indexes = {}
    # 索引内容字典
    index_content = {}

    # 来源
    source = return_block['url']
    for keyname, valuename in return_block.items():
        # 键值内容字典
        content = {}

        # url跳过
        if keyname == 'url':
            continue
        # 跳过空值
        elif len(valuename) < 1:
            continue
        # 有列表值的格式，如"Sensors / EW"
        elif keyname == "Sensors / EW" or keyname == "Weapons / Loadouts" or keyname == "Properties" or keyname == "Targets" or keyname == "Weapons":
            # 内容列表
            list_content = []
            # 内容字典
            content = {}
            # 列表内容转换
            for i in valuename:
                content["value"] = i
                content["source"] = source
                z = {}
                for i in content:
                    z[i] = content[i]
                list_content.append(z)
                index_content[keyname] = list_content
        # 默认格式转换
        else:
            content["value"] = valuename
            content["source"] = source
            index_content[keyname] = content
            # print(index_content)
    indexes[source] = index_content
    return indexes


if __name__ == '__main__':
    # 待转换文件目录路径

    # base_dir = 'data/原版'
    base_dir = 'data/冷战'

    # 文件列表
    lst_res = []
    # 结果列表
    result = []
    count = 0
    for file in os.listdir(base_dir):
        with open(os.path.join(base_dir, file), encoding='utf8') as fr:
            lst_json = json.load(fr)
            lst_res.extend(lst_json)

    # 读取数据块
    for data_block in tqdm(lst_res):
        count += 1
        return_block = remove_General_data(data_block)
        i = transform_block(return_block)
        result.append(i)

    # 写入json文件
    if base_dir == "data/原版":
        with open('../原版转格式(v1.0)' + str(count) + '.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4, ensure_ascii=False)
    elif base_dir == "data/冷战":
        with open('../冷战转格式(v1.0)' + str(count) + '.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4, ensure_ascii=False)
