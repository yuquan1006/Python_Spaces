#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 11:32
# @Author  : Yuquan
# @Site    : 
# @File    : socket_server.py
# @Software: PyCharm
import socket
# 客户端socket
'''接下来我们写一个简单的客户端实例连接到以上创建的服务。端口号为 12345。

socket.connect(hosname, port ) 方法打开一个 TCP 连接到主机为 hostname 端口为 port 的服务商。
连接后我们就可以从服务端获取数据，记住，操作完成后需要关闭连接。'''
# 创建socket对象
s = socket.socket()
#  获取本地主机名
hostName = socket.gethostname()
hostName = socket.gethostbyname(hostName)
print(hostName)
# 设置端口
port = 12345
# 连接
s.connect((hostName, port))
# 等待客户端连接

print(s.recv(1024).decode())
s.close()