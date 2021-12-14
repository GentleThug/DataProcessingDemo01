# -*- encoding: utf-8 -*-
"""
@File    :   Demo01_getRelation.py
@Contact :   wu466687121@qq.com
@License :   (C)Copyright 2020-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/9 下午2:15   SEA      1.0         WIKI舰船关系抽取
"""

# import lib
import json


def get_subclass(file_name):
    with open('wiki_data/' + file_name, 'r', encoding='utf-8') as m:
        file = json.load(m)
    data = []
    count = 0
    for i in file:
        if '舰种' in i:
            data.append(i['舰种'])
            # print('舰种：', i['舰种'])
        else:
            print('无舰种：', i['名称'])
            if '型' in i['名称']:
                data.append(i['名称'].split('型')[1])
            else:
                data.append(i['名称'].split('号')[1])

    print()
    print('小关系类数:', len(list(set(data))))
    print('小关系类:', (list(set(data))))

    with open('wiki_data/res_subclass_' + file_name, 'w', encoding='utf-8') as f:
        json.dump(list(set(data)), f, indent=4, ensure_ascii=False)
    f.close()


def get_sub_subclass():
    with open('wiki_data/res_subclass_wiki_warship_1125_modify.json', 'r', encoding='utf-8') as f:
        file1 = json.load(f)
    with open('wiki_data/res_subclass_wiki_warship_1125_origin.json', 'r', encoding='utf-8') as m:
        file2 = json.load(m)

    data = []
    dic = {}
    for i, t in enumerate(file2, 0):
        for j, k in enumerate(file1, i):
            print(j, k)

    f.close()
    m.close()
    return list(set(data))


def get_totalclass(file_name):
    with open('wiki_data/' + file_name, 'r', encoding='utf-8') as m:
        file = json.load(m)
    data = []
    count = 0
    for i in file:
        for j in i.keys():
            # print(j)
            data.append(j)

    print()
    print('关系类数:', len(list(set(data))))
    print('关系总数:', list(set(data)))

    return list(set(data))


if __name__ == '__main__':
    file_name = 'wiki_warship_1125.json'
    get_totalclass(file_name)

    # print(get_totalclass(file_name))
    # print(len(get_totalclass(file_name)))

