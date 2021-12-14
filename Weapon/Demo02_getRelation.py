# -*- encoding: utf-8 -*-
'''
@File    :   Demo01_getRelation.py
@Contact :   wu466687121@qq.com
@License :   (C)Copyright 2020-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/9 下午2:15   SEA      1.0         None
'''

# import lib
import json


if __name__ == '__main__':
    data = []
    data_count = 0
    count = 0
    filename_list = [
        'aircraft1340.json',
        'artillery540.json',
        'explosive468.json',
        'guns964.json',
        'missile466.json',
        'spaceship366.json',
        'tank546.json',
        'warship1192.json'
    ]
    for i in filename_list:
        data_mistake = []
        file_name = i

        with open('weapon_data/12.09/' + file_name, 'r', encoding='utf-8') as m:
            file = json.load(m)

        for i in file:
            for j in i['content']['技术数据']:
                for k in j.keys():
                    count += 1
                    data.append(k.replace('\xa0', '').strip().replace('\n', ''))
                    data_mistake.append(k.replace('\xa0', '').strip().replace('\n', ''))
        data_count += len(file)


        print('file_name:', file_name)
        print('data_mistake:', list(set(data_mistake)))
        print()

    print('数据条数:', data_count)
    print('关系类数:', len(list(set(data))))
    print('关系总数:', count)

    with open('relation/weapon_relation_result.json', 'w', encoding='utf-8') as f:
        json.dump(list(set(data)), f, indent=4, ensure_ascii=False)
    f.close()
