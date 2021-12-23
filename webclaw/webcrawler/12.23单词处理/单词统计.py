#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 单词统计.py    
@Time: 2021/12/22 11:29 
"""

import json
import re

if __name__ == '__main__':
    result = {}
    content = {}
    list1 = []
    count = 0
    with open('../12.22武器属性名/cmano_tilte去重（26243）.json', 'r', encoding='utf-8') as f:
        file1 = json.load(f)
    for i in file1:
        # j = i.replace("[", " ")

        j = re.sub("\d|\W", " ", i)
        j = j.split(" ")
        # j = ", ".join(j)

        for k in j:

            list1.append(k)
    for word in list1:
        if len(word) < 2:
            continue
        if len(re.findall("[^a-z]", word)) > 1:
            continue
        if word not in content:
            content[word] = 0
        content[word] += 1
    for k in sorted(content, key=content.__getitem__, reverse=True):
        # print(k, content[k])
        count += 1
        result[k] = content[k]

    # content = list(content)
    # content.sort()
    with open('cmano_tilte单词词频统计（' + str(len(content)) + '）.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
    print(json.dumps(result, indent=4, ensure_ascii=False))
    # print(content, len(content))
