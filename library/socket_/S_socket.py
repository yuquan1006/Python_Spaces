#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/13 11:25
# @Author  : Yuquan
# @Site    : 
# @File    : S_socket.py
# @Software: PyCharm
# socket 编程
import socket

# 创建tcp Socket
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("http://www.baidu.com", 80))
