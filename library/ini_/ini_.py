#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 14:27
# @Author  : Yuquan
# @Site    : 
# @File    : ini_.py
# @Software: PyCharm
# 知识点：解析ini配置文件

''' 注意：如果ini文件里面写的是数字，读出来默认是字符串


'''


# 1 python3里面自带configparser模块来读取ini文件
import configparser, os
#
# # 2.获取ini文件路经
# curpath = os.path.realpath(__file__)
# parpath = os.path.dirname(curpath)
# inipath = os.path.join(parpath, "t.ini")
#
#
# # 创建管理对象
# conf = configparser.ConfigParser()
#
#
# # read 读取
# # 读取ini文件
# conf.read(inipath, encoding="utf-8")
#
# # 获取全部section
# sections = conf.sections()
# print(sections)  # list类型
# # 获取单个
# sections = conf.options('db')
# print(sections)

# # 获取某个section下的键值对。 [(k1,v1),(k2,v2)]
# items = conf.items(sections[0])
# print(items[0])
#
# # get
# a = conf.get(sections[0],"a")
# print(a)
#
# # remove 删除section中的一项
# conf.remove_option(sections[0], "a")
# items = conf.items(sections[0])
# print(items)
# # 删除整个section这一项
# conf.remove_section(sections[0])
# sections = conf.sections()
# print(sections)
#
#
# # add
# # 1.新增一个section
# conf.add_section("s4")
# sections = conf.sections()
# print(sections)
#
# # SET
# # 2.section里面新增key和value
# conf.set("s4", "key", "value")
#
# ''' remove和set方法并没有真正的修改ini文件内容，只有当执行conf.write()方法的时候，才会修改ini文件内'''
#
# # write 写入
# # 1.conf.write(open(cfgpath, "w")) # 删除原文件重新写入
# # 2.conf.write(open(cfgpath, "a")) # 追加模式写入
# conf.write(open(inipath, "w", encoding="utf-8"))
#


# back_path = "/Users/abc/PycharmProjects/Pythoncoding/projects/"
# back_file ="hello.txt"
# 可以写为读取配置文件
# 第一步：创建conf对象
conf = configparser.ConfigParser()
# 第二步：添加section、options的值
conf.add_section("path")
conf.set("path","back_dir","/Users/abc/PycharmProjects/Pythoncoding/projects/") # option
conf.set("path","target_dir","/Users/abc/PycharmProjects/Pythoncoding/")    # option
conf.add_section("file")
conf.set("file","back_file","apitest")

# 第三步：写入文件
with open("path.ini",'w')as conffile:
    conf.write(conffile)

# 第四步：读取配置文件中的section、options的值
back_dir =conf.get('path','back_dir')
back_file =conf.get("file","back_file")
target_dir =conf.get("path","target_dir")