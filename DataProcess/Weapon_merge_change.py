# -*- encoding: utf-8 -*-
"""
@File    :   Weapon_merge_change.py
@Contact :   wu466687121@qq.com
@License :   (C)Copyright 2020-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/13 上午10:05   SEA      1.0     转换武器大全为合并格式
"""

import json

from tqdm import tqdm


# 判断结果是否有分类
def haven_noclass():
    with open('merge_data/origin/res_Weapon_data.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    count = 0
    for i in file:
        if list(i.values())[0].get('大类') == '':
            # 没有小类则打印出来 原因大部分都是QA中名称与武器大全中名称不一致，于是匹配不到分类
            print(i.keys())
            count += 1
    print('count:', count)


if __name__ == '__main__':
    data = []
    count = 0

    with open('QAonData/12.14/military（副本）.json', 'r', encoding='utf-8') as f:
        file1 = json.load(f)
    # with open('weapon_data/12.13/武器大全(12.13修改).json', 'r', encoding='utf-8') as m:
    #     file2 = json.load(m)
    with open('weapon_data/12.13/武器大全_quchong_beifen.json', 'r', encoding='utf-8') as m:
        file2 = json.load(m)

    for i in tqdm(file2):
        main_dic = {}
        main_key = i['content'].get('技术数据')[0].get('名称').replace("\t", "").strip()
        short_name = i['title']
        text = i['content'].get('text')
        # 初始化字典
        main_dic[main_key] = {
            '名称': main_key,
            '简称': short_name,
            '简介': text
        }
        # 从QA中添加分类
        for j in file1:
            # 如果QA有名称相同或十分相同的数据
            if main_key == j.get('名称') or main_key in j.get('名称') or i.get('title') in j.get('名称') or j.get(
                    '名称') in i.get('title') or j.get('名称') in main_key:
                main_dic[main_key]['小类'] = j.get('类型')
                main_dic[main_key]['大类'] = j.get('大类')
                break
        # 如果QA中也没分类的话
        if main_dic[main_key].get('小类') is None:
            # 判断武器大全源数据中是否有小分类 有则添加 无则置空
            if i.get('分类') is not None:
                main_dic[main_key]['小类'] = i['分类']
            else:
                main_dic[main_key]['小类'] = ''
            main_dic[main_key]['大类'] = ''

        # 判断是否有年代
        if i.get('年代') is not None:
            main_dic[main_key]['年代'] = i.get('年代')
        # 存url
        if i.get('url') is not None:
            main_dic[main_key]['url'] = i.get('url')
        # 存国家
        if i.get('国家') is not None:
            main_dic[main_key]['国家'] = i.get('国家')
        # 存入技术数据中其他key
        for j, t in enumerate(i['content'].get('技术数据')):
            if j > 0:
                main_dic[main_key][list(t.items())[0][0]] = list(t.items())[0][1]
        # 存入content中其他key
        for j in i['content']:
            if j != 'text' and j != '技术数据':
                main_dic[main_key][j] = i['content'].get(j)

        data.append(main_dic)

    with open('merge_data/12.14/res_Weapon_data_qvchong_12.14.json', 'w', encoding='utf-8') as f:
        # with open('merge_data/res_Weapon_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    f.close()
    haven_noclass()
