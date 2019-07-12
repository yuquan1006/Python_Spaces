#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
import json

# json字符串中安装json格式的字符串  如json中布尔值：true和false都是小写 python中True和False
# 字典转json字符串
d = {
    "name": 18973019192,
    "passwd": 2566321,
    "cc": "chandao"
}
print(d)
print(type(d))
d_json = json.dumps(d)
print(d_json)
print(type(d_json))
# json字符串转化字典
d = '{"name": 18973019192,"passwd": 2566321,"cc": "chandao"}'
d_str = json.loads(d)
print(type(d_str))

# eval 函数把字符串当成代码执行
a = "100+200"
a = eval(a)
print(a)
# 普通字符串转化成字典
a = '{"name": 18973019192,"passwd": 2566321,"cc": True}'
a =eval(a)
print(type(a))

from urllib.parse import unquote

# unquote 将url编码妆花成中文
# unquote(url)
import time
