# -*- encoding: utf-8 -*-
"""
@File    :   Test_class.py
@Contact :   wu466687121@qq.com
@License :   (C)Copyright 2020-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/13 下午3:50   SEA      1.0         None
"""
import json
import jieba


def getLen():
    with open('merge_data/origin/res_Weapon_data.json', 'r', encoding='utf-8') as f:
        file1 = json.load(f)
    with open('merge_data/origin/res_QA_Data.json', 'r', encoding='utf-8') as f:
        file2 = json.load(f)
    with open('merge_data/12.13/res_Weapon_data_qvchong.json', 'r', encoding='utf-8') as m:
        file3 = json.load(m)
    with open('weapon_data/12.13/武器大全(12.13修改).json', 'r', encoding='utf-8') as m:
        file4 = json.load(m)
    with open('QAonData/origin/military.json', 'r', encoding='utf-8') as m:
        file5 = json.load(m)

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
    count = 0
    for i in filename_list:
        file_name = i
        with open('weapon_data/12.09/' + file_name, 'r', encoding='utf-8') as m:
            file = json.load(m)
        count += len(file)

    print('WeaponRES_LEN：', len(file1))
    print('QARES_LEN：', len(file2))
    print('WeaponRES_qvchong_LEN：', len(file3))
    print('武器大全(12.13修改)_LEN：', len(file4))
    print('QA_LEN：', len(file5))
    print(count)


# 获取武器大全头实体总数
def weapon_total_headclass():
    with open('merge_data/12.13/res_Weapon_data_qvchong.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    for i in file:
        print(list(list(i.values())[0].keys()))


# 比较QA和武器大全中数据
def compare():
    with open('merge_data/12.14/res_Weapon_data_qvchong_12.14.json', 'r', encoding='utf-8') as f:
        file1 = json.load(f)
    with open('merge_data/12.14/res_QA_Data_fuben.json', 'r', encoding='utf-8') as m:
        file2 = json.load(m)

    count = 0

    for i in file2:
        flag = False
        for j in file1:
            if list(i.keys())[0] == list(j.keys())[0]:
                flag = True
                break
        if not flag:
            print(list(i.keys())[0])
            count += 1
            pass
    print(count)


# 武器大全查找重复数据
def military_qvchong():
    dic = {}
    count = 0
    with open('merge_data/12.14/res_Weapon_data_qvchong_12.14.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    for i in file:
        if list(i.keys())[0] not in dic:
            dic[list(i.keys())[0]] = 1
        else:
            dic[list(i.keys())[0]] += 1
    for i, t in dic.items():
        if t >= 2:
            print(i, t)
            count += 1
    print(count)


# QA查找重复数据
def QA_qvchong():
    dic = {}
    count = 0
    with open('merge_data/12.14/res_QA_Data_fuben.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    for i in file:
        if list(i.keys())[0] not in dic:
            dic[list(i.keys())[0]] = 1
        else:
            dic[list(i.keys())[0]] += 1
    for i, t in dic.items():
        if t >= 2:
            print(i, t)
            count += 1
    print(count)


# 查找武器大全中公共属性
def military_public():
    dic = {}
    count = 0
    with open('merge_data/12.14/res_Weapon_data_qvchong_12.14.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    for i in file:
        for j in i.values():
            for k, t in j.items():
                if k not in dic:
                    dic[k] = 1
                else:
                    dic[k] += 1

    print(sorted(dic.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))


# 查找QA中公共属性
def QA_public():
    dic = {}
    count = 0
    with open('merge_data/12.14/res_QA_Data_fuben.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    for i in file:
        for j in i.values():
            for k, t in j.items():
                if k not in dic:
                    dic[k] = 1
                else:
                    dic[k] += 1

    print(sorted(dic.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))

# 查找cmano重复数据
def filter_program_data(file_name):
    data = []
    dic = {}
    with open('cmano_data/12.5cmano_合并/' + file_name, 'r', encoding='utf-8') as f:
        file = json.load(f)

    for i in file:
        if i['title'] not in dic:
            dic[i['title']] = 1
        else:
            dic[i['title']] += 1
    data.append(dic)
    with open('cmano_data/12.16_filter/res_filter_' + file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    f.close()


# 筛选出title重复的数据
def filter_program(file_name):
    data = []
    with open('cmano_data/12.16_filter/' + file_name, 'r', encoding='utf-8') as f:
        file = json.load(f)
    for i in file:
        for j, t in i.items():
            if t >= 2:
                dic = {
                    "title": j,
                    "times": t
                }
                data.append(dic)
    with open('cmano_data/12.16_filter/duplicate_data/res_' + file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    f.close()


def get_different():
    data = []
    with open('cmano_data/12.15cmano原数据/submarine全部646.json', 'r', encoding='utf-8') as f:
        file1 = json.load(f)
    with open('cmano_coldwar_data/12.14_origin/submarine_cw全部519.json', 'r', encoding='utf-8') as m:
        file2 = json.load(m)
    dic = {
        "冷战多": 0,
        "cmano": 0
    }

    for i in file1:
        for j in file2:
            if i['title'] == j['title']:
                if i['Country/Type'] == j['Country/Type']:
                    if len(i['General data:']) > len(j['General data:']):
                        dic['cmano'] += 1
                    else:
                        dic['冷战多'] += 1
    print(dic)
    # with open('cmano_data/12.16_country_same/res_country_submarine', 'w', encoding='utf-8') as f:
    #     json.dump(data, f, indent=4, ensure_ascii=False)
    # f.close()
    # with open('cmano_data/12.16_country_same/res_country_aircraft', 'r', encoding='utf-8') as m:
    #     file3 = json.load(m)
    # print(len(file3))


def is_chinese(string):
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True

    return False


def weapon_cmano_compare():
    file_list = [
        'res_aircraft整合9069.json',
        'res_facility整合5674.json',
        'res_sensor整合6208.json',
        'res_ship整合5840.json',
        'res_submarine整合1165.json',
        'res_weapon整合3715.json',
    ]
    with open('weapon_data/12.13/武器大全_quchong_beifen.json', 'r', encoding='utf-8') as f:
        file1 = json.load(f)
    for i in file_list:
        with open('cmano_data/12.15_translate/' + i, 'r', encoding='utf-8') as f:
            file2 = json.load(f)
        for j in file2:
            jieba_res = jieba.lcut(j['名称'])
            print(jieba_res)
            for k in jieba_res:
                if is_chinese(k):
                    pass

if __name__ == '__main__':
    # getLen()
    # weapon_total_headclass()
    # compare()
    # military_qvchong()
    # QA_qvchong()
    # military_public()
    # QA_public()
    # filter_program_data('weapon整合3715.json')
    # filter_program('res_filter_weapon整合3715.json')
    # weapon_cmano_compare()
    get_different()
    pass
