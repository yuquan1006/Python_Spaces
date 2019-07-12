#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 15:02
# @Author  : Yuquan
# @Site    : 
# @File    : demo_json.py
# @Software: PyCharm
'''
JSON:JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，易于人阅读和编写。
学习目标：如何使用 Python 语言来编码和解码 JSON 对象。
'''

import json
'''
json.dumps	将 Python 对象编码成 JSON 字符串
json.loads	将已编码的 JSON 字符串解码为 Python 对象
'''

# 1.dumps: 用于将 Python 对象编码成 JSON 字符串
# 列表 -- > json字符串
list_01 = [{"a":1,"b":2,"c":3},{"A":1,"B":2,"C":3}]
print(type(list_01))
print(list_01)
newlist_01 = json.dumps(list_01, indent=4)  # indent 缩进格式
newlist_02 = json.dumps(list_01, separators=(",", ":"))  # 参数separators(元素分隔符，对象键值分隔符)。一般python存储都是元素分隔符,+空格 对象键值分隔符:+空格。可以separator去掉空格。

print(type(newlist_01))
print(newlist_01)
print(newlist_02)

# 1.dumps: 用于将 Python 对象编码成 JSON 字符串
#  字典 -- > json字符串
dict_01 = {"phone":"18973019192","pwd":"yu1234","keep":True}
print(type(json.dumps(dict_01)))
print(json.dumps(dict_01))

'''
python 原始类型向 json 类型的转化对照表：
Python	            JSON
dict	            object
list, tuple	        array
str, unicode	    string
int, long, float	number
True	            true
False	            false
None	            null
'''

# 2 loads:用于解码 JSON 数据。该函数返回 Python 字段的数据类型。
#
json_data = '{"phone": "18973019192", "pwd": "yu1234", "keep": true}'
new_data = json.loads(json_data)
print(new_data)
print(type(new_data))

'''
json 类型转换到 python 的类型对照表：
同上，反过来即可
'''
a = "1234"
print(a[1::])
def test():
    try:
        while True:
            num = int(input('input num'))
            if not isinstance(num,int):
                print('input Error')
                continue
            strs = str(num)
            if not strs.startswith("-1"):
                strs = strs[::-1]
                return strs
            strs = strs[1::]
            strs = strs[::-1]
            result = "-"+strs

            return result
    except:
        print('input Error')
        raise

# print(test())
import random
