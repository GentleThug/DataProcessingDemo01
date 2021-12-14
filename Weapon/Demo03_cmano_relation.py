# -*- encoding: utf-8 -*-
'''
@File    :   Demo01_getRelation.py
@Contact :   wu466687121@qq.com
@License :   (C)Copyright 2020-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/9 下午2:15   SEA      1.0         None
'''

# import lib
import json


if __name__ == '__main__':
    data = []
    count = 0
    filename_list = [
        'aircraft全部5246.json',
        'facility全部3325.json',
        'sensor全部6236.json',
        'ship全部3394.json',
        'submarine全部647.json',
        'weapon全部3727.json'
    ]

    for i in filename_list:
        file_name = i

        with open('cmano_data/' + file_name, 'r', encoding='utf-8') as m:
            file = json.load(m)

        for j in file:
            for k in j['General data:']:
                for l in k.keys():
                    data.append(l)
                    count += 1

    print('关系类数:', len(list(set(data))))
    print('关系总数:', count)

    with open('relation/cmano_relation_result.json', 'w', encoding='utf-8') as f:
        json.dump(list(set(data)), f, indent=4, ensure_ascii=False)
    f.close()
