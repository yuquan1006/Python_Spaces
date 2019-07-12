#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/30 17:16
# @Author  : Yuquan
# @Site    : 
# @File    : mysqlCmd.py
# @Software: PyCharm
import MySQLdb
class MysqlCmd(object):
    def clear_position(self,num,numlist,host='xx.xx.xx.x',port=3306,username='xx',password='x'):
        conn = MySQLdb.connect(
            host = host,
            port = port,
            user = username,
            passwd = password,
            db = 'xx'
        )
        cur = conn.cursor()
        for i in range(num):
            cur.execute(numlist[i])

        cur.close()
        conn.commit()
        conn.close()


