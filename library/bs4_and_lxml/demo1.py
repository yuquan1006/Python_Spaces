#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 14:57
# @Author  : Yuquan
# @Site    : 
# @File    : Practice02.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import requests
soup = BeautifulSoup(requests.get("http://699pic.com/zhuanti/meinvxiezhen.html",headers={}).content, "html.parser")
print(soup)