#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 单词导出.py    
@Time: 2021/12/23 10:59 
"""
#!/usr/bin/env python
# -*-coding:utf-8 -*-

import json
import re

if __name__ == '__main__':
    result = []
    content = {}
    count = 0
    with open('cmano_tilte去重（26243）.json', 'r', encoding='utf-8') as f:
        file1 = json.load(f)
    for i in file1:
        # j = i.replace("[", " ")

        j = re.sub("\d|\W", " ", i)
        j = j.split(" ")
        # j = ", ".join(j)

        for k in j:
            count += 1
            content[k] = 1
    content = list(content)
    content.sort()
    with open('cmano_tilte单词（' + str(len(content)) + '）.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=4, ensure_ascii=False)
    # print(json.dumps(result, indent=4, ensure_ascii=False))
    print(content, len(content))
