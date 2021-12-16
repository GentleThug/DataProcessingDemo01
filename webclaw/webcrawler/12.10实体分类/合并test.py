#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 合并test.py    
@Time: 2021/12/11 15:38 
"""
import json

if __name__ == '__main__':
    # with open('data_save/type_relations_quchong.json', 'r', encoding='utf-8') as f:
    #     data = json.load(f)
    con = []
    content = {}
    data = [
        {"title": "Saab-35龙",
            "分类：": "战斗机"},
        {"title": "X-35",
            "分类：": "战斗机"},
        {"title": "X-35",
            "年代：": "冷战后至今"},
        {"title": "Saab-35龙",
            "年代：": "二战"},
        {"title": "Saab-35龙",
            "气动布局：": "三角面"},
        {"title": "X-35",
         "气动布局：": "111"},
    ]
    result = data
    # 遍历title值
    for i in range(len(result)):
        title_name = result[i]['title']
        # 遍历，进行比对
        for j in range(len(result)):
            j_name = result[j]['title']
            # 如果title相等
            if j_name == title_name:
                # 将title相等的字典元素都放在content中
                content['title'] = result[i]['title']
                for k, h in result[j].items():
                    content[k] = h
            if j == len(result):
                break

        print(content)








            # if j_name == title_name:
            #     for k, h in result[i].items():
            #         content[k] = h

    # with open('type/type_relations_quchong.json', 'w', encoding='utf-8') as f:
    #     json.dump(con, f, indent=4, ensure_ascii=False)
    # print(json.dumps(con, indent=4, ensure_ascii=False))
