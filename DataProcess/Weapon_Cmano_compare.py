# -*- encoding: utf-8 -*-
"""
@File    :   Weapon_Cmano_compare.py    
@Contact :   wu466687121@qq.com
@License :   (C)Copyright 2020-2021

    @Modify Time       @Author    @Version   @Desciption
-------------------   ---------   ---------   -----------
2021/12/17 上午11:26       SEA         1.0         None
"""
import json
import nltk


def weapon_cmano_compare_origin():
    file_list = [
        'res_aircraft整合9069.json',
        # 'res_facility整合5674.json',
        # 'res_sensor整合6208.json',
        # 'res_ship整合5840.json',
        # 'res_submarine整合1165.json',
        # 'res_weapon整合3715.json',
    ]
    for i in file_list:
        with open('cmano_data/12.15_translate/' + i, 'r', encoding='utf-8') as f:
            file = json.load(f)
        for j in file:
            print("原名称：", j['名称'])
            # 根据中文逗号split
            split_douhao = j['名称'].split('，')[0]
            step_1 = [str(j) for j in split_douhao]
            step_2 = ''.join(step_1)
            # print(HanLP.extractKeyword(j['名称'], len(j['名称'].split('，'))))

            # 根据中文括号split
            split_kuohao = step_2.split("（")[0]
            step_3 = [str(j) for j in split_kuohao]
            step_4 = ''.join(step_3)

            # 根据英文中括号split
            split_en_zhongkuohao = step_4.split("[")[0]
            step_5 = [str(j) for j in split_en_zhongkuohao]
            step_6 = ''.join(step_5)

            # 根据中文中括号split
            split_ch_zhongkuohao = step_6.split("【")[0]
            step_7 = [str(j) for j in split_ch_zhongkuohao]
            step_8 = ''.join(step_7)

            print("名称处理后：", step_8)
            # print("分关键词：", HanLP.extractKeyword(step_8, len(step_8)))
            # print("分词：", HanLP.segment(step_6))
            print()

def weapon_cmano_compare():
    file_list = [
        'res_aircraft整合9069.json',
        # 'res_facility整合5674.json',
        # 'res_sensor整合6208.json',
        # 'res_ship整合5840.json',
        # 'res_submarine整合1165.json',
        # 'res_weapon整合3715.json',
    ]
    for i in file_list:
        with open('cmano_data/12.15_translate/' + i, 'r', encoding='utf-8') as f:
            file = json.load(f)
        for j in file:
            print("原title：", j['title'])
            # 根据中文逗号split
            split_douhao = j['title'].split('，')[0]
            step_1 = [str(j) for j in split_douhao]
            step_2 = ''.join(step_1)
            # print(HanLP.extractKeyword(j['名称'], len(j['名称'].split('，'))))

            # 根据中文括号split
            split_kuohao = step_2.split("（")[0]
            step_3 = [str(j) for j in split_kuohao]
            step_4 = ''.join(step_3)

            # 根据英文中括号split
            split_en_zhongkuohao = step_4.split("[")[0]
            step_5 = [str(j) for j in split_en_zhongkuohao]
            step_6 = ''.join(step_5)

            # 根据中文中括号split
            split_ch_zhongkuohao = step_6.split("【")[0]
            step_7 = [str(j) for j in split_ch_zhongkuohao]
            step_8 = ''.join(step_7)

            split_gang = step_6.split(" - ")[0]
            step_9 = [str(j) for j in split_gang]
            step_10 = ''.join(step_9)

            print("title处理后：", step_10)
            # print("分关键词：", HanLP.extractKeyword(step_8, len(step_8)))
            print("分词：", nltk.word_tokenize(step_10))
            print()

if __name__ == '__main__':
    # weapon_cmano_compare()
    # NLTK分词
    # sentence = "Motor Rifle Plt (BTR-82A APC x 3)"
    # tokens = nltk.word_tokenize(sentence)
    # print(tokens)
    weapon_cmano_compare()
    pass