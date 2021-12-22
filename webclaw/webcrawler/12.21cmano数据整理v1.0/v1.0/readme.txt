cmano数据处理v1.0版本
@Author: 李晋源
---------------------

版本简介:

本次版本内容主要是对cmano原版和冷战的原始数据格式进行转换处理
其中冷战数据共有9173条,原版数据共有22507条
---------------------

目录结构说明：

########### 目录结构
v1.0
  ├─ readme.txt                            // 说明文档
  ├─ src
  │  ├─ data                               // 原始数据目录
  │  │  ├─ 冷战
  │  │  │  ├─ aircraft_cw全部3836.json
  │  │  │  ├─ facility_cw全部2360.json
  │  │  │  ├─ ship_cw全部2458.json
  │  │  │  └─ submarine_cw全部519.json
  │  │  └─ 原版
  │  │     ├─ aircraft全部5231.json
  │  │     ├─ facility全部3314.json
  │  │     ├─ sensor全部6208.json
  │  │     ├─ ship全部3382.json
  │  │     ├─ submarine全部646.json
  │  │     └─ weapon全部3726.json
  │  └─ 转格式.py                           // 转格式程序
  ├─ 冷战转格式(v1.0)9173.json
  └─ 原版转格式(v1.0)22507.json

src目录下,存放程序代码以及冷战和原版的初始格式json文档
所有原始数据都在src/data目录下
根目录下存放冷战和原版的转换格式后的json文档
所有json文件名中的数字表示其内含的数据条数
---------------------

程序说明：

主函数下base_dir变量代表待转换数据文件的目录路径（不同原数据需手动切换路径）
文件输入输出代码都添加注释，附上了切换文件的代码
--------
函数用法：

remove_General_data()：
去除General_data这一级属性，将内容全部取出
整体数据变为source：{keyname：{}}二级结构

transform_block()：
处理remove_General_data函数得到的数据块
主要是注意 有列表值的属性格式，如"Sensors / EW"等，需要添加列表保存多个字典
默认数据处理为source：{keyname：{"value": "valuename", "source": "source"}}结构
有列表值的属性格式处理为source：{keyname：[{"value": "valuename", "source": "source"}]结构
---------------------

常见问题：

未用代码统一格式化json格式，输出文档的结构不够简洁
需要注意手动切换写入路径,如果更改默认数据路径，请注意查看写入json代码是否一致
程序运行时进度条显示的是已转换格式的条数，还需等待写入数据过程结束，文档才会生成
