# -*- encoding: utf-8 -*-
"""
@File    :   Demo08_Weapon_excel.py    
@Contact :   wu466687121@qq.com
@License :   (C)Copyright 2020-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/12/12 下午4:29   SEA      1.0         None
"""

import csv

# 获取ｊｓｏｎ数据
import json

with open('weapon_data/12.09/aircraft1340.json', 'r') as f:
    rows = json.load(f)

# 创建文件对象
f = open('weapon_data/12.13/aircraft1340.csv', 'w')

# 通过文件创建csv对象
csv_write = csv.writer(f)

# writerow: 按行写入，　writerows: 是批量写入
# 写入数据 取列表的第一行字典，用字典的ｋｅｙ值做为头行数据
# print(rows[0])
data = []
# data.append()
csv_write.writerow(rows[0].keys())

# 循环里面的字典，将value作为数据写入进去
for row in rows:
    csv_write.writerow(row.values())

# 关闭打开的文件
f.close()
