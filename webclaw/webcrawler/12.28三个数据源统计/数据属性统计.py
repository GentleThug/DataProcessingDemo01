#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 数据属性统计.py    
@Time: 2021/12/28 10:12 
"""
import json
import os

from tqdm import tqdm

def show_count():
    with open('../../../data/武器大全/res_Weapon_data_qvchong_12.14.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    list1 = []
    count = 0
    for i in file:
        for k, v in i.items():
            list1.append(v.keys())
    for i in list1:
        for j in i:
            print(j)
            count += 1
            # if j not in list2:
            #     list2.append(j)

    return count


# 获取武器大全中所有属性名
def get_Relation1():
    with open('../../../data/武器大全/res_Weapon_data_qvchong_12.14.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    list1 = []
    list2 = []
    for i in file:
        for k, v in i.items():
            # if v.get('大类') == "舰船舰艇":
                # print(v.get('小类'))
                list1.append(v.keys())

        # for k in i.values():
        #     if k.values() == "飞行器":
        #         k.get()
        #             aircraft.append(list(k.keys()))
        #     list1.append(list(k.keys()))

    for i in list1:
        for j in i:
            if j not in list2:
                list2.append(j)
    # print(list2)
    list2 = list(set(list2))
    list2.sort()
    return list2


def get_Relation2(dir):
    with open(dir, 'r', encoding='utf-8') as f:
        file = json.load(f)
    data = []
    for data_block in tqdm(file):
        result = {}
        for keyname, valuename in data_block.items():
            if keyname == 'General data':
                for i_key, i_value in valuename[0].items():
                    result[i_key] = i_value
            else:
                result[keyname] = valuename
            data.append(result)
    list1 = []

    for i in data:
        for k, v in i.items():
            # print(k,v)
            if k == "Type":
                list1.append(v)
    list1 = list(set(list1))
    list1.sort()
    return list1

def get_Relation3(dir):
    with open(dir, 'r', encoding='utf-8') as f:
        file = json.load(f)
    data = []
    for data_block in tqdm(file):
        result = {}
        for keyname, valuename in data_block.items():
            if keyname == 'General data':
                for i_key, i_value in valuename[0].items():
                    result[i_key] = i_value
            # else:
            #     result[keyname] = valuename
            data.append(result)
    list1 = []

    for i in data:
        for k, v in i.items():
            # if k == "Type":
                list1.append(k)
    list1 = list(set(list1))
    list1.sort()
    # print(list1)
    # for k in sorted(list1, key=list1.__getitem__, reverse=True):
    #     # print(k, content[k])
    #     content[k] = list1[k]
    return list1

def os_open():
    base_dir = '../../../data/cmano/原版'
    # base_dir = '../../../data/cmano/冷战'
    # 文件列表
    lst_res = []
    # 结果列表
    result = []
    count = 0
    for file in os.listdir(base_dir):
        with open(os.path.join(base_dir, file), encoding='utf8') as fr:
            lst_json = json.load(fr)
            lst_res.extend(lst_json)
    data = []
    for data_block in tqdm(lst_res):
        result = {}
        for keyname, valuename in data_block.items():
            if keyname == 'General data':
                for i_key, i_value in valuename[0].items():
                    result[i_key] = i_value
            # else:
            #     result[keyname] = valuename
            data.append(result)
    list1 = []

    for i in data:
        for k, v in i.items():
            # if k == "Type":
                list1.append(k)
    list1 = list(set(list1))
    list1.sort()
    # print(list1)
    # for k in sorted(list1, key=list1.__getitem__, reverse=True):
    #     # print(k, content[k])
    #     content[k] = list1[k]
    return list1

def os_show():
    base_dir = '../../../data/cmano/原版'
    # base_dir = '../../../data/cmano/冷战'
    # 文件列表
    lst_res = []
    # 结果列表
    result = []
    count = 0
    for file in os.listdir(base_dir):
        with open(os.path.join(base_dir, file), encoding='utf8') as fr:
            lst_json = json.load(fr)
            lst_res.extend(lst_json)
    data = []
    for data_block in tqdm(lst_res):
        result = {}
        for keyname, valuename in data_block.items():
            if keyname == 'General data':
                for i_key, i_value in valuename[0].items():
                    result[i_key] = i_value
            else:
                result[keyname] = valuename
        data.append(result)
    # print(json.dumps(data, indent=4, ensure_ascii=False))
    print(len(data))


    for i in data:
        for k, v in i.items():
            # print(k,v)
            count += 1


    return count

if __name__ == '__main__':
    # print(get_Relation2())
    dir = "../../../data/cmano/原版/weapon全部3727.json"
    print(os_show())
    # print(json.dumps(get_Relation1(), indent=0, ensure_ascii=False),'\n',len(get_Relation1()))
    # print(json.dumps(get_Relation2(dir), indent=0, ensure_ascii=False),'\n',len(get_Relation2(dir)))
    # print(json.dumps(get_Relation3(dir), indent=0, ensure_ascii=False), '\n', len(get_Relation3(dir)))
    # print(json.dumps(os_open(), indent=0, ensure_ascii=False), '\n', len(os_open()))

