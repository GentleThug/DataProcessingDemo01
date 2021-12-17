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
    base_dir = '冷战cmano对比'
    for file in os.listdir(base_dir):
        with open(os.path.join(base_dir, file), encoding='utf8') as fr:
            lst_json = json.load(fr)
            lst_res.extend(lst_json)
    with open('对比结果_1216.txt', 'w', encoding='utf8') as fw:
        for dic in lst_res:
            if dic['different_data'] == '数据相同':
                continue
            name = dic['title']
            Country_Type = dic['Country/Type']

            fw.write('装备名：{}\n'.format(name))
            fw.write('原版与冷战中所属国家：{}\n'.format(Country_Type))
            for d in dic['different_data']:
                if "国家" in d.keys():
                    print( list(d.values()))
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
                        fw.write('{:30}\t{:30}\t{:30}\n'.format(key, '-', value))
                if "cmano多的属性" in d.keys():
                    for key, value in d['cmano多的属性'].items():
                        fw.write('{:30}\t{:30}\t{:30}\n'.format(key, value, '-'))
            fw.write('\n\n\n')