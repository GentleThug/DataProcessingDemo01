# -*- encoding: utf-8 -*-
"""
@File    :   Weapon_getRelation.py    
@Contact :   wu466687121@qq.com
@License :   (C)Copyright 2020-2021

    @Modify Time       @Author    @Version   @Desciption
-------------------   ---------   ---------   -----------
2021/12/17 下午4:31       SEA         1.0         None
"""
import json

from tqdm import tqdm

from Weapon_translate import translate_weapon_BaiduAPI


def show_count():
    with open('weapon_data/12.13/武器大全_quchong_beifen.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    dic = {}
    for i in file:
        for j in i['content'].get('技术数据'):
            if list(j.keys())[0] not in dic:
                dic[list(j.keys())[0]] = 0
            dic[list(j.keys())[0]] += 1
            # print(list(j.keys())[0])
    return dic


# 获取武器大全中所有关系
def get_Relation1():
    with open('weapon_data/12.13/武器大全_quchong_beifen.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    data = []
    list2 = []
    list1 = []
    for i in file:
        for j in i['content'].get('技术数据'):
            list1.append(list(j.keys())[0])

    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2


def get_Relation2():
    with open('merge_data/12.14/res_Weapon_data_qvchong_12.14.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    data = []
    list2 = []
    list1 = []
    for i in file:
        for j, t in (i.get(list(i.keys())[0])).items():
            list1.append(j)

    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2


def translate_en_relation():
    with open('weapon_data/12.17/sorted_relation/武器大全有序关系输出.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    data = []
    for i in tqdm(file):
        data.append(translate_weapon_BaiduAPI(i))
    return data


if __name__ == '__main__':
    # print(get_Relation2())
    # print(get_Relation1())
    with open('weapon_data/12.17/sorted_relation/武器大全_原始数据_有序关系输出.json', 'w', encoding='utf-8') as f:
        json.dump(get_Relation1(), f, indent=4, ensure_ascii=False)
    f.close()
    # with open('weapon_data/12.17/sorted_relation/武器大全有序关系_转英文输出.json', 'w', encoding='utf-8') as f:
    #     json.dump(translate_en_relation(), f, indent=4, ensure_ascii=False)
    # f.close()
    # with open('weapon_data/12.17/sorted_relation/武器大全有序关系_转英文输出.json', 'w', encoding='utf-8') as f:
    #     json.dump(translate_en_relation(), f, indent=4, ensure_ascii=False)
    # f.close()