#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 11:32
# @Author  : Yuquan
# @Site    : 
# @File    : socket_server.py
# @Software: PyCharm
import socket
# 服务端socket
'''我们使用 socket 模块的 socket 函数来创建一个 socket 对象。socket 对象可以通过调用其他函数来设置一个 socket 服务。

现在我们可以通过调用 bind(hostname, port) 函数来指定服务的 port(端口)。

接着，我们调用 socket 对象的 accept 方法。该方法等待客户端的连接，并返回 connection 对象，表示已连接到客户端。'''

# 创建socket对象
s = socket.socket()
#  获取本地主机名
hostName = socket.gethostname()
hostName = socket.gethostbyname(hostName)
print(hostName)
# 设置端口
port = 12345
# 绑定端口
s.bind((hostName,port))
# 等待客户端连接
s.listen(5)
while True:
    print('waiting for connection...')
    conn, addr = s.accept() # 接受连接。套接字必须绑定到一个地址并侦听连接。返回值是一对，其中conn是可用于在连接上发送和接收数据的 新套接字对象， address是绑定到连接另一端的套接字的地址。(conn, address)
    print('...connected from:',addr)
    conn.send("欢迎访问!".encode())
    conn.send("我的地址!".encode())
    conn.close()  # 关闭连接
