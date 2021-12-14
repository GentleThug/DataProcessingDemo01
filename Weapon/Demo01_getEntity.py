# -*- encoding: utf-8 -*-
'''
@File    :   Demo01_getEntity.py
@Contact :   wu466687121@qq.com
@License :   (C)Copyright 2020-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/9 下午2:15   SEA      1.0         None
'''

# import lib
import json

file_name = 'warship1192.json'
with open('weapon_data/' + file_name, 'r', encoding='utf-8') as m:
    file = json.load(m)

if __name__ == '__main__':
    data = []
    for i in file:
        data.append(i['title'].split('_')[0].strip())

    with open('main_entity/entity_' + file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    f.close()
