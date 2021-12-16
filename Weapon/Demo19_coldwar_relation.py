# -*- encoding: utf-8 -*-
"""
@File    :   Demo19_coldwar_relation.py    
@Contact :   wu466687121@qq.com
@License :   (C)Copyright 2020-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/15 下午5:39   SEA      1.0         None
"""
import json


def getClass(filelist):
    data = []
    for i in filelist:

        with open('cmano_coldwar_data/12.14_origin/' + i, 'r', encoding='utf-8') as m:
            file = json.load(m)
        for j in file:
            data.append(j['General data:'][0].get('Type'))

    with open('cmano_coldwar_data/12.15_relation/res_Class.json', 'w', encoding='utf-8') as f:
        json.dump(list(set(data)), f, indent=4, ensure_ascii=False)
    f.close()
    print(len(list(set(data))))


def getRelation(filelist):
    data = []
    for i in filelist:

        with open('cmano_coldwar_data/12.14_origin/' + i, 'r', encoding='utf-8') as m:
            file = json.load(m)
        for j in file:
            for k in list(j['General data:'][0].keys()):
                data.append(k)

    with open('cmano_coldwar_data/12.15_relation/res_total.json', 'w', encoding='utf-8') as f:
        json.dump(list(set(data)), f, indent=4, ensure_ascii=False)
    f.close()
    print(len(list(set(data))))


if __name__ == '__main__':
    relation = []
    filename_list = [
            'aircraft_cw全部3836.json',
            'facility_cw全部2360.json',
            'ship_cw全部2458.json',
            'submarine_cw全部519.json'
        ]
    # getRelation(filename_list)
    getClass(filename_list)
