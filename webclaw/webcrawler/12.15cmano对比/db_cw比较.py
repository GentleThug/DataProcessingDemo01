#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: db_cw比较.py    
@Time: 2021/12/15 9:29 
"""
import json

if __name__ == '__main__':
    # with open('cmano_cw/submarine_cw全部519.json', 'r', encoding='utf-8') as f:
    #     file1 = json.load(f)
    # with open('cmano_db/submarine全部646.json', 'r', encoding='utf-8') as f:
    #     file2 = json.load(f)
    with open('1.json', 'r', encoding='utf-8') as f:
        file1 = json.load(f)
    with open('2.json', 'r', encoding='utf-8') as f:
        file2 = json.load(f)
    count = 0
    data = []
    con = {}
    # 冷战
    for i in file1:
        # DB
        for j in file2:
            different_data = []
            # 名称相同？
            if i['title'] == j['title']:
                con['title'] = i['title']
                # 国家相同？
                if i['Country/Type'] == j['Country/Type']:
                    con['Country/Type'] = '相同'
                    con['different_data'] = ""
                else:
                    con['Country/Type'] = '不同'
                    country = {}
                    different_country = {}
                    different_country['冷战'] = i['Country/Type']
                    different_country['cmano'] = j['Country/Type']
                    country["country"] = different_country
                    different_data.append(country)

                # 一般属性相同?
                if i['General data'] == j['General data']:
                    con['General data'] = '相同'

                else:
                    # 公共属性数据
                    common_data = {}
                    # 不同属性值
                    cw_box = {}
                    db_box = {}
                    z = {}
                    cw_flag = 0
                    db_flag = 0
                    cw_data = {}
                    db_data = {}
                    # k,h是key  l,g是value
                    for k, l in i['General data'][0].items():
                        # 是否出现从未比对过的key
                        flagi = 0
                        for h, g in j['General data'][0].items():
                            # key相等
                            if k == h:
                                # 只要j和i的key匹配上了
                                flagi += 1
                                # 且values相等
                                if l == g:
                                    common_data[k] = l
                                    z['冷战和cmano的公共属性'] = common_data
                                # values不等
                                else:
                                    # 不同的其他属性值
                                    other_data = {}
                                    other_data["冷战"] = l
                                    other_data["cmano"] = g
                                    common_data[k] = other_data
                                    z['冷战和cmano的公共属性'] = common_data

                        if flagi == 0:
                            # 冷战多的属性

                            cw_data[k] = l
                        cw_box["冷战多的属性"] = cw_data

                    if len(list(list(cw_box.values())[0].keys())) > 0:
                        different_data.append(cw_box)

                    for h, g in j['General data'][0].items():
                        # 是否出现从未比对过的key
                        flagj = 0
                        for k, l in i['General data'][0].items():
                            if k == h:
                                # 只要j和i的key匹配上了
                                flagj += 1

                        if flagj == 0:
                            # cmano多的属性

                            db_data[h] = g
                        db_box["cmano多的属性"] = db_data
                    if len(list(list(db_box.values())[0].keys())) > 0:
                        different_data.append(db_box)
                    different_data.append(z)
                z = {}
                con['different_data'] = different_data
                for n in con.keys():
                    z[n] = con[n]

                data.append(z)

            # data.append(con)


    # with open('cmano_db_cw/aircraft重复数据' + str(len(con)//2) + '条（国家一样）.json', 'w', encoding='utf-8') as f:
    #     json.dump(con, f, indent=4, ensure_ascii=False)
    print(json.dumps(data, indent=4, ensure_ascii=False))
