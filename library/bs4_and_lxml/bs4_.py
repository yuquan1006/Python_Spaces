#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 10:43
# @Author  : Yuquan
# @Site    : 
# @File    : bs4_.py
# @Software: PyCharm
import requests,os
from bs4 import BeautifulSoup

html = open("htmldemo.html",encoding="utf-8")
# soup对象：整个html对象
soup = BeautifulSoup(html, "html.parser")
# print(soup)
print(type(soup))

# 标签对象：例如 <p class="title"><b>yoyoketang</b></p>
tag = soup.body
# print(tag)
tag = soup.head
print(tag)
print(type(tag))

# 字符串对象 (获取便签内文本)
str = tag.string
print(str)


# 通过便签名获取tag对象；有多个便签名，返回的是第一个
tag = soup.title
print(tag)

# 获取标签的所有属性 由于class属性一般可以为多个，中间空格隔开，所以class属性获取的是一个list类型：[u'sister']
tag = soup.a
print(tag)
print(tag.attrs)
print(tag.attrs['class'][0])

# find_all 查找标签对象，返回的是列表
tag = soup.find_all(class_="sister")
print(tag)

# get_text 获取tag便签下所有的文本
print(tag[0].get_text())




# 下载图片案例
url = "http://699pic.com/sousuo-218808-13-1.html"
r = requests.get(url)
# print(r.text)
soup = BeautifulSoup(r.content, "html.parser")
# print(soup)
img_tag = soup.find_all(class_='lazy')
print(img_tag)
cur = os.path.realpath(__file__)
print(cur)
par = os.path.dirname(cur)
print(par)
img_flo = os.path.join(par, "img")
if not os.path.exists(img_flo):
    os.mkdir(img_flo)
print(img_flo)
for i in img_tag:
    try:
        jpg_url = i.get("data-original")
        print(jpg_url)
        title = i.get("title")
        print(title)
        img_path = os.path.join(img_flo, "%s.jpg" % title)
        print(img_path)
        with open(img_path, "wb") as f:
            f.write(requests.get(jpg_url).content)


    except:
        pass


