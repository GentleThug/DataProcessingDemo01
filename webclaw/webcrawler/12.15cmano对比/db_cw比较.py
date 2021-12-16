#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@Author: LJY
@File: db_cw比较.py    
@Time: 2021/12/15 9:29 
"""
import json

if __name__ == '__main__':
    with open('cmano_cw/aircraft_cw全部3838.json', 'r', encoding='utf-8') as f:
        file1 = json.load(f)
    with open('cmano_db/aircraft全部5231.json', 'r', encoding='utf-8') as f:
        file2 = json.load(f)
    count = 0
    con = []
    data = []
    for i in range(len(file1)):
        for j in range(len(file2)):
            # if file1[i]['title'] == file2[j]['title']:
            #     count += 1
            #     break
                # print(file2[j]['title'] )
            if file1[i]['title'] == file2[j]['title']:
                # print( file1[i]['title'] ,file2[j]['title'])

                if file1[i]['Country/Type'] == file2[j]['Country/Type']:
                    con.append(file1[i])
                    con.append(file2[j])
                else:
                    print(file1[i]['title'])


                    # con["Country/Type"] = '相同'

                #
                # for k in  range(len(file1[i]['General data'])):
                #     file1_date = file1[i]['General data'][k]
                #     for l in  range(len(file2[j]['General data'])):
                #         file2_date = file2[j]['General data'][l]
                #         if list(file1_date.keys())[k] == list(file2_date.keys())[l]:
                #             if list(file1_date.values())[k] == list(file2_date.values())[l]:
                #                 typecount += 1
                #             con["data"] = typecount

                count += 1
                break
            # data.append(con)
    # print(count)
    with open('cmano_db_cw/aircraft重复数据' + str(len(con)//2) + '条（国家一样）.json', 'w', encoding='utf-8') as f:
        json.dump(con, f, indent=4, ensure_ascii=False)
    # print(json.dumps(con, indent=4, ensure_ascii=False))
