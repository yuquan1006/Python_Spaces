#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 9:36
# @Author  : Yuquan
# @Site    : 
# @File    : xml_.py
# @Software: PyCharm
import os
# 知识点：解析xml

# 1.从硬盘中加载xml文件
import xml.etree.ElementTree as ET
parse = ET.parse(os.path.join(os.path.dirname(os.path.realpath(__file__)), "demo.xml_"))

# 2.从字符串中读取  【注意】fromstring()是直接获取string对象中的根节点，因此以上root其实是一个Element
# 作为一个Element对象，本身是具有子元素，因此可以直接对Element进行迭代取值：或者通过索引找子节点
root = ET.fromstring('<collection shelf="New Arrivals">中国文本</collection>')
print(root.text)
# 获取根节点
root = parse.getroot()
print(root.tag )

root.set("key1","value1")
for i in root.items():
    print(i)
tag_list = []
for i in root.iter():
    print(i.tag)
    tag_list.append(i.tag)
tag_list = list(set(tag_list))
print(tag_list)





# Element.iter(tag=None)：遍历该Element所有后代，也可以指定tag进行遍历寻找。
#
# Element.findall(path)：查找当前元素下tag或path能够匹配的直系节点。
#
# Element.find(path)：查找当前元素下tag或path能够匹配的首个直系节点。
#
# Element.text: 获取当前元素的text值。
#
# Element.get(key, default=None)：获取元素指定key对应的属性值，如果没有该属性，则返回default值。
#
#  Element对象 

#
#
# 　　tag：string，元素代表的数据种类。
# 　　text：string，元素的内容。
# 　　tail：string，元素的尾形。
# 　　attrib：dictionary，元素的属性字典。
# 　　
# 　　＃针对属性的操作
# 　　clear()：清空元素的后代、属性、text和tail也设置为None。
# 　　get(key, default=None)：获取key对应的属性值，如该属性不存在则返回default值。
# 　　items()：根据属性字典返回一个列表，列表元素为(key, value）。
# 　　keys()：返回包含所有元素属性键的列表。
# 　　set(key, value)：设置新的属性键与值。
#
#
# 　　＃针对后代的操作
# 　　append(subelement)：添加直系子元素。
# 　　extend(subelements)：增加一串元素对象作为子元素。＃python2.7新特性
# 　　find(match)：寻找第一个匹配子元素，匹配对象可以为tag或path。
# 　　findall(match)：寻找所有匹配子元素，匹配对象可以为tag或path。
# 　　findtext(match)：寻找第一个匹配子元素，返回其text值。匹配对象可以为tag或path。
# 　　insert(index, element)：在指定位置插入子元素。
# 　　iter(tag=None)：生成遍历当前元素所有后代或者给定tag的后代的迭代器。＃python2.7新特性
# 　　iterfind(match)：根据tag或path查找所有的后代。
# 　　itertext()：遍历所有后代并返回text值。
# 　　remove(subelement)：删除子元素。





#
# if __name__ == '__main__':
#     a = os.path.join(os.path.dirname(os.path.realpath(__file__)), "demo.xml_")
#     print(a)