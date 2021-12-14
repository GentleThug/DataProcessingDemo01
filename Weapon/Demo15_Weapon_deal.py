# -*- encoding: utf-8 -*-
"""
@File    :   Demo15_Weapon_deal.py
@Contact :   wu466687121@qq.com
@License :   (C)Copyright 2020-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/13 上午10:05   SEA      1.0         None
"""

import json

# def

if __name__ == '__main__':
    data = []

    file_name = 'military.json'

    with open('weapon_data/12.13/武器大全(12.13修改).json', 'r', encoding='utf-8') as m:
        file = json.load(m)
    count = 0
    for i in file:
        if i.get('content') == None:
            # print(i)
            pass
        if i.get('分类') == None:
            # print(i)
            # print(i['content'].get('技术数据')[0])
            # count += 1
            # data.append(i['content'].get('技术数据')[0].values())
            pass
        if i.get('国家') == None:
            print(i)
            count += 1
            # print(i['content'].get('技术数据')[0])
            # data.append(i['content'].get('技术数据')[0].values())
            pass
        if i.get('年代') == None:
            # print(i)
            # count += 1
            # print(i['content'].get('技术数据')[0])
            # data.append(i['content'].get('技术数据')[0].values())
            pass

    print(count)

    # with open('weapon_data/res_military.json', 'w', encoding='utf-8') as f:
    #     json.dump(data, f, indent=4, ensure_ascii=False)
    # f.close()