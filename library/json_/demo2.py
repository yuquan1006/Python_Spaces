#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 11:40
# @Author  : Yuquan
# @Site    : 
# @File    : demo2.py
# @Software: PyCharm

# json.dump	将 Python 对象写入到json文件
# json.load	读取json文件为 Python 对象
#
import json
data = {
            "name":"余泉",
            "age":12,
            "people":True
        }

# 写入到文件保存json数据类型
with open("demo.json", "w",encoding='utf-8') as f:
    json.dump(data, f)

# 从文件中读取且转成python数据类型
with open("demo.json", 'r',encoding='utf-8') as f:
    d = json.load(f)
    print(d)
