#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 14:30
# @Author  : Yuquan
# @Site    : 
# @File    : yaml01.py
# @Software: PyCharm
# yaml简介：yaml 是专门用来写配置文件的语言，非常简洁和强大,之前用ini也能写配置文件，看了yaml后，发现这个更直观，更方便，有点类似于json格式

import yaml
import os
# 读yaml文件
# filePath = os.path.join(os.path.dirname(os.path.realpath(__file__)),"test.yaml")
# print(filePath)
# f = open(filePath, encoding='utf-8')
# cfg = f.read()
# print(type(cfg))  # 读出来是字符串
#
# res = yaml.load(cfg)
# print(type(res))  # 读出来是列表/字典  根据yaml文件中数据的格式定
# print(res)
# f.close()
# for i in res:
#     if isinstance(i, dict):
#         url = i['url']
#         method = i['method']
#         print(url,method)

# # 写yaml
# data = [
#     {"url":"/xxxx",
#      "method":"post",
#      "age": 11}]
# filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)),"t1.yaml")
# f = open(filepath,"w",encoding='utf-8')
# yaml.dump(data,f)
# f.close()
# 运行完之后，发现字典嵌套的字典，出现了大括号：{androidProcess: 'com.tencent.mm:tools'}，
# 这不是真正的yaml数据，不是我们想要的，解决办法:    pip install ruamel.yaml


# from ruamel import yaml
# data = [
#     {"url":"/xxxx",
#      "method":"post",
#      "age": 11}]
# filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)),"t1.yaml")
# f = open(filepath,"w",encoding='utf-8')
# yaml.dump(data,Dumper=yaml.RoundTripDumper,stream=f)
# f.close()

