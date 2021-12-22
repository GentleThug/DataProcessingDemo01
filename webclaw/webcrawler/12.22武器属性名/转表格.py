#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 转表格.py    
@Time: 2021/12/22 11:17 
"""
#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 导出title.py    
@Time: 2021/12/22 9:30 
"""
import json
import os
import lwxl

if __name__ == '__main__':


    base_dir = '../../../data/cmano/merge'
    # 文件列表
    lst_res = []
    # 结果列表
    result = []
    content = {}
    count = 0
    with open('base_dir', 'r', encoding='utf-8') as f:
        lst_json = json.load(f)
    for data_block in tqdm(lst_res):
        for keyname, valuename in data_block.items():
            if keyname == "title":
                count += 1
                content[valuename] = count
                result.append(valuename)
    content = list(content)
    with open('tilte去重（' + str(len(content)) + '）.json', 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=4, ensure_ascii=False)
    with open('tilte（' + str(len(result)) + '）.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
    # print(json.dumps(content, indent=4, ensure_ascii=False))
    # print(len(content))