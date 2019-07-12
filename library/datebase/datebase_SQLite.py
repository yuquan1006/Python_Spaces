#!/usr/bin/env python
# encoding: utf-8
# author: 余泉
# version: python3.6
# file: datebase_SQLite.py
# time: 2018\4\25 0025 17:00

# 数据库           通过SQLite了解数据库操作
import sqlite3
conn = sqlite3.connect('database.db')       # 创建数据库      使用基础数据库系统，首先必须连接到它，这个时候需要使用具有名称的connect函数,connect函数返回连接对象。这个对象表示目前和数据库的会话
cu = conn.cursor()                           # 获取能连接的游标，这个游标可以用来执行SQL查询。   cursor 返回连接的游标对象
# 创建数据表
# cu.execute('''create table Person(id integer primary key ,
# Name varchar(20) UNIQUE,
# Age integer
# )
# ''')
# 插入数据
# cu.execute("insert into Person values (1,'余泉',25)")
# cu.execute("insert into Person values (2,'余安',26)")
conn.commit()                                #             完成插入并且做出某些更改后确保已经进行了提交，这样才可以将这些修改真正地保存到文件中
# 查询数据
cu.execute("select * from Person")
print(cu.fetchall())
cu.execute("select id,name from Person")
print(cu.fetchall())
# 修改
cu.execute("update Person set age = 10 where id = 1")
cu.execute("select * from Person")
print(cu.fetchall())
# 删除
cu.execute("delete from Person WHERE id=2")
cu.execute("select * from Person")
print(cu.fetchall())
cu.close()