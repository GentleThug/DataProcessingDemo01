# -*- coding: UTF-8 -*-
"""
describe:
@author: LSW66
@file: test2.py
@time: 2021/11/27/9:19
"""
import json
import random
import re
import time
import urllib.request
import urllib.parse

from lxml import etree

def pipei_title():
    title ="综合监视系统关键技术专利信息研究招标公告"
    pepei = re.search("系统",title)
    print(pepei)
    if pepei:
        content = title
        print(content)

if __name__ == '__main__':
    pipei_title()