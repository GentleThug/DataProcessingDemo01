#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: data_test.py    
@Time: 2021/12/10 13:43 
"""
import re
from bs4 import BeautifulSoup
import requests
import json

if __name__ == '__main__':
    url = 'https://wuqi.supfree.net/' + "ufo.asp?classify=aircraft&type=%E6%88%98%E6%96%97%E6%9C%BA"
    response = requests.get(url)
    print(url)
    response.encoding = 'UTF-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    page_text = soup.find(class_="ulink").text
    page_num = re.search("(\d{1,3})页", page_text).group()
    print(page_text)
    print(page_num)