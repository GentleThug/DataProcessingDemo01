# -*- encoding: utf-8 -*-
"""
@File    :   Demo16_Test.py    
@Contact :   wu466687121@qq.com
@License :   (C)Copyright 2020-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/13 下午3:50   SEA      1.0         None
"""
import json
from tqdm import tqdm

with open('QAonData/12.14/military（副本）.json', 'r', encoding='utf-8') as f:
    file = json.load(f)

if __name__ == '__main__':
    data = []
    main_dic = {}

    for i in file:
        print(i)
        main_dic = {}
        main_key = i['名称'].strip()
        main_dic[main_key] = {
            '名称': main_key,
            '小类': i['类型'],
            '大类': i['大类'],
            '产国': i['产国'],
            '图片': i['图片'],
            '简介': i['简介']
        }
        for j, t in i.items():
            if j != '名称' and j != '类型' and j != '大类' and j != '产国' and j != '图片' and j != '简介' and j != '_id':
                main_dic[main_key][j] = t
        data.append(main_dic)

    with open('merge_data/12.14/res_QA_Data_fuben.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    f.close()