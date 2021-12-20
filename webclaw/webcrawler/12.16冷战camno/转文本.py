#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 转文本.py    
@Time: 3021/12/16 21:40 
"""
import json
import os


if __name__ == '__main__':
    lst_res = []
    cw_type = {}
    db_type = {}
    bt_type = {}
    base_dir = '冷战cmano对比'
    for file in os.listdir(base_dir):
        with open(os.path.join(base_dir, file), encoding='utf8') as fr:
            lst_json = json.load(fr)
            lst_res.extend(lst_json)
    count = buxiangtong = name_num= 0
    with open('对比结果_1217.txt', 'w', encoding='utf8') as fw:
        for dic in lst_res:
            if dic['different_data'] == '数据相同':
                count += 1
                # print(dic['different_data'] )
                continue
            else:
                buxiangtong += 1
            name = dic['title']
            Country_Type = dic['Country/Type']
            name_num += 1
            fw.write('序号：{}\n'.format(name_num))
            fw.write('装备名：{}\n'.format(name))
            fw.write('原版与冷战中所属国家：{}\n'.format(Country_Type))
            for d in dic['different_data']:
                if "国家" in d.keys():
                    # print( list(d.values()))
                    fw.write('所属国家：{}\n'.format(str(list(d.values())[0])))
            fw.write('{:30}\t{:30}\t{:30}\n'.format('属性名', 'cmano', '冷战'))
            for d in dic['different_data']:
                if "country" in d.keys():
                    for key, value in d['country'].items():
                        if key == '冷战':
                            cw = value
                            if len(cw) < 2:
                                cw = '-'
                        if key == 'cmano':
                            db = value
                    fw.write('{:30}\t{:30}\t{:30}\n'.format('国家', cw, value))
                if "冷战多的属性" in d.keys():
                    for key, value in d['冷战多的属性'].items():
                        if key not in cw_type:
                            cw_type[key] = 0
                        cw_type[key] += 1
                        fw.write('{:30}\t{:30}\t{:30}\n'.format(key, '-', value))
                if "cmano多的属性" in d.keys():
                    for key, value in d['cmano多的属性'].items():
                        if key not in db_type:
                            db_type[key] = 0
                        db_type[key] += 1
                        fw.write('{:30}\t{:30}\t{:30}\n'.format(key, value, '-'))
                if "冷战和cmano的公共属性" in d.keys():
                    for key, value in d['冷战和cmano的公共属性'].items():
                        if type(value) == dict:
                            if key not in bt_type:
                                bt_type[key] = 0
                            bt_type[key] += 1
                            value1 =[]
                            for h, g in value.items():
                                value1.append(g)
                            fw.write('{:30}\t{:30}\t{:30}\n'.format(key, value1[1], value1[0]))
            fw.write('\n\n\n')
    print(count)
    print(buxiangtong)
    print(cw_type)
    print(db_type)
    print(bt_type)
