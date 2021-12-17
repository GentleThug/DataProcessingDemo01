# -*- encoding: utf-8 -*-
"""
@File    :   merge.py    
@Contact :   wu466687121@qq.com
@License :   (C)Copyright 2020-2021

    @Modify Time       @Author    @Version   @Desciption
-------------------   ---------   ---------   -----------
2021/12/16 下午10:10       SEA         1.0         None
"""
import json
import os

lst_res = []
base_dir = '/home/root1/PycharmProjects/DataProcessingDemo01/webclaw/webcrawler/12.16冷战camno/冷战cmano对比/V1.0/'
for file in os.listdir(base_dir):
    with open(os.path.join(base_dir, file), encoding='utf8') as fr:
        lst_json = json.load(fr)
        lst_res.extend(lst_json)
with open('./对比结果_1216.txt', 'w', encoding='utf8') as fw:
    for dic in lst_res:
        # print(dic)
        if dic['different_data'] == '相同':
            continue
        name = dic['title']
        print(dic)
        print(dic['different_data'][0].get('country'))
        Country_Type = dic['Country/Type']
        fw.write('装备名：{}\n'.format(name))
        fw.write('\t\t\t\t\t\tcmano\t\t\t\t\t冷战\n')
        fw.write('原版与冷战中所属国家：{}\n'.format(Country_Type))
        for d in dic['different_data']:
            if "冷战多的属性" in d.keys():
                for key, value in d['冷战多的属性'].items():
                    fw.write('{:20}\t{:20}\t{:20}\n'.format(key, '-', value))
            if "cmano多的属性" in d.keys():
                for key, value in d['cmano多的属性'].items():
                    fw.write('{:20}\t{:20}\t{:20}\n'.format(key, value, '-'))
        fw.write('\n\n\n')