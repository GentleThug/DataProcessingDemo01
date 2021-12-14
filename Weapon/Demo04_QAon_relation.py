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
    class_data = {}
    dic_property = {}
    count = 0
    file_name = 'military.json'


    with open('QAonData/' + file_name, 'r', encoding='utf-8') as m:
        file = json.load(m)

    for i in file:
        if i['大类'] not in class_data:
            class_data[i['大类']] = ''
        elif i['类型'] not in class_data[i['大类']]:
            count += 1
            class_data[i['大类']] += i['类型'] + ','
    for i in class_data.values():
        print(i)
        print(len(i.split(',')) - 1)
    print(class_data)
    print(count)


    # with open('QAonData/relation_result_' + file_name, 'w', encoding='utf-8') as f:
    #     json.dump(list(set(data)), f, indent=4, ensure_ascii=False)
    # f.close()
