# -*- encoding: utf-8 -*-
"""
@File    :   Demo16_Test.py    
@Contact :   wu466687121@qq.com
@License :   (C)Copyright 2020-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/13 下午3:50   SEA      1.0         None
"""
import json


def getLen():
    with open('merge_data/res_Weapon_data.json', 'r', encoding='utf-8') as f:
        file1 = json.load(f)
    with open('merge_data/res_QA_Data.json', 'r', encoding='utf-8') as f:
        file2 = json.load(f)
    with open('merge_data/res_Weapon_data_qvchong.json', 'r', encoding='utf-8') as m:
        file3 = json.load(m)
    with open('weapon_data/12.13/武器大全(12.13修改).json', 'r', encoding='utf-8') as m:
        file4 = json.load(m)
    with open('QAonData/military.json', 'r', encoding='utf-8') as m:
        file5 = json.load(m)

    filename_list = [
        'aircraft1340.json',
        'artillery540.json',
        'explosive468.json',
        'guns964.json',
        'missile466.json',
        'spaceship366.json',
        'tank546.json',
        'warship1192.json'
    ]
    count = 0
    for i in filename_list:
        file_name = i
        with open('weapon_data/12.09/' + file_name, 'r', encoding='utf-8') as m:
            file = json.load(m)
        count += len(file)

    print('WeaponRES_LEN：', len(file1))
    print('QARES_LEN：', len(file2))
    print('WeaponRES_qvchong_LEN：', len(file3))
    print('武器大全(12.13修改)_LEN：', len(file4))
    print('QA_LEN：', len(file5))
    print(count)


# 获取武器大全头实体总数
def weapon_total_headclass():
    with open('merge_data/res_Weapon_data_qvchong.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    for i in file:
        print(list(list(i.values())[0].keys()))


# 比较QA和武器大全中数据
def compare():
    with open('merge_data/res_Weapon_data_qvchong_12.14.json', 'r', encoding='utf-8') as f:
        file1 = json.load(f)
    with open('merge_data/res_QA_Data_fuben.json', 'r', encoding='utf-8') as m:
        file2 = json.load(m)

    count = 0

    for i in file2:
        flag = False
        for j in file1:
            if list(i.keys())[0] == list(j.keys())[0]:
                flag = True
                break
        if not flag:
            print(list(i.keys())[0])
            count += 1
            pass
    print(count)


# 武器大全查找重复数据
def military_qvchong():
    dic = {}
    count = 0
    with open('merge_data/res_Weapon_data_qvchong_12.14.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    for i in file:
        if list(i.keys())[0] not in dic:
            dic[list(i.keys())[0]] = 1
        else:
            dic[list(i.keys())[0]] += 1
    for i, t in dic.items():
        if t >= 2:
            print(i, t)
            count += 1
    print(count)


# QA查找重复数据
def QA_qvchong():
    dic = {}
    count = 0
    with open('merge_data/res_QA_Data_fuben.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    for i in file:
        if list(i.keys())[0] not in dic:
            dic[list(i.keys())[0]] = 1
        else:
            dic[list(i.keys())[0]] += 1
    for i, t in dic.items():
        if t >= 2:
            print(i, t)
            count += 1
    print(count)


# 查找武器大全中公共属性
def military_public():
    dic = {}
    count = 0
    with open('merge_data/res_Weapon_data_qvchong_12.14.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    for i in file:
        for j in i.values():
            for k, t in j.items():
                if k not in dic:
                    dic[k] = 1
                else:
                    dic[k] += 1

    print(sorted(dic.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))


# 查找QA中公共属性
def QA_public():
    dic = {}
    count = 0
    with open('merge_data/res_QA_Data_fuben.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    for i in file:
        for j in i.values():
            for k, t in j.items():
                if k not in dic:
                    dic[k] = 1
                else:
                    dic[k] += 1

    print(sorted(dic.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))


if __name__ == '__main__':
    # getLen()
    # weapon_total_headclass()
    # compare()
    # military_qvchong()
    # QA_qvchong()
    military_public()
    # QA_public()
    pass
