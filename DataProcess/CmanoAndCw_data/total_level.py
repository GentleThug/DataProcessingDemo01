# -*- encoding: utf-8 -*-
"""
@File    :   total_level.py    
@Contact :   wu466687121@qq.com
@License :   (C)Copyright 2020-2021

    @Modify Time       @Author    @Version   @Desciption
-------------------   ---------   ---------   -----------
2021/12/17 下午2:32       SEA         1.0         None
"""
import json


if __name__ == '__main__':

    dic = {
        'General data': [],
        'Properties': []
    }

    file_list = [
        'aircraft_merge.json',
        'facility_merge.json',
        'sensor_merge.json',
        'ship_merge.json',
        'submarine_merge.json',
        'weapon_merge.json'
    ]
    for filename in file_list:
        with open('cmano_cw_mergeData/' + filename, 'r', encoding='utf-8') as f:
            file = json.load(f)
        for i in file:
            for j, t in i.items():
                if j != 'title' and j != 'url' and j != 'Country/Type':
                    if j not in dic:
                        dic[j] = []
    print(dic)

    pass