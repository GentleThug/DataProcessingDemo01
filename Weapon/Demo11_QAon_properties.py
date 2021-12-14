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
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data6 = []
    data7 = []
    data8 = []
    dic_property = {}
    file_name = 'military.json'


    with open('QAonData/' + file_name, 'r', encoding='utf-8') as m:
        file = json.load(m)

    for i in file:
        class_name = i['大类']
        # print(i.keys())
        if class_name == '飞行器':
            for j in i.keys():
                data1.append(j)
        if class_name == '火炮':
            for j in i.keys():
                data2.append(j)
        if class_name == '爆炸物':
            for j in i.keys():
                data3.append(j)
        if class_name == '枪械与单兵':
            for j in i.keys():
                data4.append(j)
        if class_name == '导弹武器':
            for j in i.keys():
                data5.append(j)
        if class_name == '太空装备':
            for j in i.keys():
                data6.append(j)
        if class_name == '坦克装甲车辆':
            for j in i.keys():
                data7.append(j)
        if class_name == '舰船舰艇':
            for j in i.keys():
                data8.append(j)

    print(list(set(data1)))
    print(len(list(set(data1))))

    print(list(set(data2)))
    print(len(list(set(data2))))

    print(list(set(data3)))
    print(len(list(set(data3))))

    print(list(set(data4)))
    print(len(list(set(data4))))

    print(list(set(data5)))
    print(len(list(set(data5))))

    print(list(set(data6)))
    print(len(list(set(data6))))

    print(list(set(data7)))
    print(len(list(set(data7))))

    print(list(set(data8)))
    print(len(list(set(data8))))

    with open('QAonData/12.13/relation_result_' + '飞行器' + file_name, 'w', encoding='utf-8') as f:
        json.dump(list(set(data1)), f, indent=4, ensure_ascii=False)
    f.close()
    with open('QAonData/12.13/relation_result_' + '火炮' + file_name, 'w', encoding='utf-8') as f:
        json.dump(list(set(data2)), f, indent=4, ensure_ascii=False)
    f.close()
    with open('QAonData/12.13/relation_result_' + '爆炸物' + file_name, 'w', encoding='utf-8') as f:
        json.dump(list(set(data3)), f, indent=4, ensure_ascii=False)
    f.close()
    with open('QAonData/12.13/relation_result_' + '枪械与单兵' + file_name, 'w', encoding='utf-8') as f:
        json.dump(list(set(data4)), f, indent=4, ensure_ascii=False)
    f.close()
    with open('QAonData/12.13/relation_result_' + '导弹武器' + file_name, 'w', encoding='utf-8') as f:
        json.dump(list(set(data5)), f, indent=4, ensure_ascii=False)
    f.close()
    with open('QAonData/12.13/relation_result_' + '太空装备' + file_name, 'w', encoding='utf-8') as f:
        json.dump(list(set(data6)), f, indent=4, ensure_ascii=False)
    f.close()
    with open('QAonData/12.13/relation_result_' + '坦克装甲车辆' + file_name, 'w', encoding='utf-8') as f:
        json.dump(list(set(data7)), f, indent=4, ensure_ascii=False)
    f.close()
    with open('QAonData/12.13/relation_result_' + '舰船舰艇' + file_name, 'w', encoding='utf-8') as f:
        json.dump(list(set(data8)), f, indent=4, ensure_ascii=False)
    f.close()
