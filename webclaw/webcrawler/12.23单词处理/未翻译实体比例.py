#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: 未翻译实体比例.py    
@Time: 2021/12/23 19:28 
"""
import csv

if __name__ == '__main__':
    with open('实体名翻译v0.1.csv') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            print(row)