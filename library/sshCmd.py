#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/7 10:57
# @Author  : Yuquan
# @Site    :
# @File    : sshCmd.py
# @Software: PyCharm
# pamamiko 模块

import paramiko

class sshCmd(object):
    def sshClient_execmd(self,host,port,username,password,execmd):
        #
        paramiko.util.log_to_file(r"C:\Users\A\Desktop\paramiko.log")
        # 实例化客户端
        client = paramiko.SSHClient()
        # 自动添加策虐，保持服务器主机和密匙信息
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        # 加载服务器密匙
        client.load_system_host_keys()
        # 连接服务器，以用户名和密码
        client.connect(host,port,username,password)
        # 打开一个chan（实例化的transport，并建立会话），并执行命令   chan = self._transport.open_session(timeout=timeout)
        stdin,stdout,stderr = client.exec_command(execmd)
        stdin.write("Y")
        print(stdout.read())
        client.close()

if __name__ == '__main__':
    s = sshCmd()
    s.sshClient_execmd("192.168.199.100",22,"root","123456","mkdir /test.txt")
    s.sshClient_execmd("192.168.199.100",22,"root","123456","rm -rf /test.txt")
