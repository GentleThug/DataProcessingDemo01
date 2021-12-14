# -*- encoding: utf-8 -*-
"""
@File    :   Demo07_cmano_getClass.py.py    
@Contact :   wu466687121@qq.com
@License :   (C)Copyright 2020-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/10 下午4:47   SEA      1.0         None
"""

import json

# def

if __name__ == '__main__':
    data = []
    data1 = []

    filename_list = [
        'aircraft全部5246.json',
        'facility全部3325.json',
        'sensor全部6236.json',
        'ship全部3394.json',
        'submarine全部647.json',
        'weapon全部3727.json'
    ]

    for file_name in filename_list:
        data1 = []
        with open('cmano_data/' + file_name, 'r', encoding='utf-8') as m:
            file = json.load(m)
        for i in file:
            # print(i['Country/Type'])
            # data.append(i['Country/Type'])
            for j in i['General data:']:
                for key, value in j.items():
                    if key == 'Type':
                        data1.append(value.strip())
                        data.append(value.strip())
        print(file_name + ':', end="")
        print(len(list(set(data1))))
        print(list(set(data1)))
        print()

    print(len(list(set(data))))
    print(list(set(data)))
    with open('cmano_data/res_cmano_modify1.json', 'w', encoding='utf-8') as f:
        json.dump(list(set(data)), f, indent=4, ensure_ascii=False)
    f.close()