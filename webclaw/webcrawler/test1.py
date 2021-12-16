# -*- encoding: utf-8 -*-
"""
@File    :   test1.py    
@Contact :   wu466687121@qq.com
@License :   (C)Copyright 2020-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/14 下午6:11   SEA      1.0         None
"""
import json


def cw_strip(file_list):
    for i in file_list:
        with open('12.15cmano对比/cmano_cw/' + i, 'r', encoding='utf-8') as f:
            file = json.load(f)
        for j in file:
            for k, l in j['General data'][0].items():
                j['General data'][0].update({k: l.strip()})
        with open('12.15cmano对比/cmano_cw/12.16_stripBlank/' + i, 'w', encoding='utf-8') as f:
            json.dump(file, f, indent=4, ensure_ascii=False)
        f.close()


def cmano_strip(file_list):
    for i in file_list:
        with open('12.15cmano对比/cmano_db/' + i, 'r', encoding='utf-8') as f:
            file = json.load(f)
        for j in file:
            for k, l in j['General data'][0].items():
                j['General data'][0].update({k: l.strip()})
        with open('12.15cmano对比/cmano_db/12.16_stripBlank/' + i, 'w', encoding='utf-8') as f:
            json.dump(file, f, indent=4, ensure_ascii=False)
        f.close()
        print(len(file))


if __name__ == '__main__':
    cw_list = [
        'aircraft_cw全部3838.json',
        'facility_cw全部2360.json',
        'ship_cw全部2458.json',
        'submarine_cw全部519.json'
    ]

    cmano_list = [
        'aircraft全部5231.json',
        'facility全部3314.json',
        'sensor全部6208.json',
        'ship全部3382.json',
        'submarine全部646.json',
        'weapon全部3715.json',

    ]
    # cw_strip(cw_list)
    cmano_strip(cmano_list)
