#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: remove_capital.py    
@Time: 2021/12/23 9:29 
"""
import json
import re
from tqdm import tqdm

if __name__ == "__main__":
    with open("cmano_tilte单词（10138）.json", 'r', encoding='utf-8') as f:
        file1 = json.load(f)
    result = []
    for words in tqdm(file1):
        # if len(re.findall("\W", words)) > 1:
        #     print(re.findall("\W", words))
        #     continue
        if len(words) < 2:
            continue
        if len(re.findall("[^a-z]", words)) > 1:
            continue
        else:
            result.append(words)
        # print(words)
    result.sort()
    # print(json.dumps(result, indent=4, ensure_ascii=False))
    with open('cmano_tilte单词（' + str(len(result)) + '）.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
