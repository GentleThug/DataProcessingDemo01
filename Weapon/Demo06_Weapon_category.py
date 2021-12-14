# -*- encoding: utf-8 -*-
"""
@File    :   Demo06_Weapon_category.py
@Contact :   wu466687121@qq.com
@License :   (C)Copyright 2020-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/10 上午11:21   SEA      1.0         None
"""
import json

if __name__ == '__main__':
    data = []
    dic_mainclass = {}

    file_name = 'type_all.json'
    with open('weapon_data/12.10/' + file_name, 'r', encoding='utf-8') as m:
        file = json.load(m)

    count = 0
    for i in file:
        dic_divclass = {}
        for j in i.items():
            for k, t in enumerate(j):
                dic_divclass[j[0]] = j[1]
                if j[0] != '类别':
                    dic_divclass[j[0] + 'len'] = len(j[1])
                if j[0] == '分类：':
                    count += len(j[1])
                    print(j[1])
                break

        data.append(dic_divclass)
    print("关系总数：", count)
    with open('weapon_data/res_class_' + file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    f.close()