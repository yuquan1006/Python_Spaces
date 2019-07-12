#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 10:59
# @Author  : Yuquan
# @Site    : 
# @File    : pymysql_.py
# @Software: PyCharm
import pymysql

# 1.打开数据库连接（ip/数据库用户名/登录密码/数据库名）
# db = pymysql.connect("127.0.0.1", "root", "123456", "test")

# 2.使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()

# 3.使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
# print("Database version : %s " % data)

# 3.1 查询数据
# sql = "SELECT * FROM t1"
# try:
#     # 执行
#     cursor.execute(sql)
#     # 获取所有记录列表结果:[(id,name,xxx),(id2,name2,xx)]
#     result = cursor.fetchall()
#     for row in result:
#         id = row[0]
#         name = row[1]
#         print("id=%s,name=%s" % (id, name))
# except:
#     print("查询失败")

# 3.2 插入数据
# sql = "INSERT INTO t1(id,name) VALUES(4,\"小孩子\");"
# try:
#     # 执行
#     cursor.execute(sql)
#     # 提交到数据库执行
#     db.commit()
# except:
#     # 如果发生错误则回滚
#     db.rollback()

# 3.3 更新数据
# sql = "UPDATE t1 SET name = 'Bob' WHERE id = 1"
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 提交到数据库执行
#     db.commit()
# except:
#     # 发生错误时回滚
#     db.rollback()

# 3.4 删除数据
# sql = "DELETE FROM t1 WHERE id  = 4"
# try:
    # 执行SQL语句
    # cursor.execute(sql)
    # 提交修改
    # db.commit()
# except:
    # 发生错误时回滚
    # db.rollback()




# 4.关闭数据库连接
# db.close()




class MysqlCmd(object):
    def __init__(self,host,port,user,pwd,db): #类的构造函数，初始化数据库连接ip或者域名，以及用户名，密码，要连接的数据库名称
        self.host=host
        self.port = port
        self.user=user
        self.pwd=pwd
        self.db=db
    def __GetConnect(self):  #得到数据库连接信息函数， 返回: conn.cursor()
        self.conn=pymysql.connect(host=self.host,port = self.port,user=self.user,password=self.pwd,database=self.db,charset='utf8')
        cur=self.conn.cursor()  #将数据库连接信息，赋值给cur。
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def queryMysqlDatas(self,sql):
        '''执行查询语句,返回的是一个包含tuple的tuple，外层tuple的元素是记录行，内部tuple的元素是每行记录的字段'''
        # 获得数据库连接信息
        cur = self.__GetConnect()
        # 执行Sql语句
        cur.execute(sql)
        print('开始执行【查询多行】mysql语句:%s'%sql)
        # 获得所有的查询结果
        result_list = cur.fetchall()
        # 查询完毕后必须关闭连接
        self.conn.close()
        # 返回查询结果
        return result_list


    def queryMysqlData(self,sql):
        '''执行查询语句，返回一行数据（tuple（id，name，xx，xxxx））'''
        cur = self.__GetConnect()
        cur.execute(sql)
        print('开始执行【查询单行】mysql语句:%s'%sql)

        result = cur.fetchone()
        self.conn.close()
        return result

    def insertMysqlData(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        print('开始执行【插入】mysql语句:%s'%sql)
        self.conn.commit()
        self.conn.close()

    def updateMysqlData(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        print('开始执行【更新】mysql语句:%s'%sql)
        self.conn.commit()
        self.conn.close()

    def tranckMysqlData(self,tableNum,tableList):
        '''删除全部数据，不能与where连用'''
        cur = self.__GetConnect()

        for i in range(tableNum):
            cur.execute("truncate table %s" % tableList[i])
            print('开始执行[删除]mysql语句:%s' % "truncate table %s" % tableList[i] )
        self.conn.commit()
        self.conn.close()

    def deleteMysqlData(self,sql):
        '''只是删除表中某些数据，表结构还在.不与where一起用，既删除全部数据'''
        cur = self.__GetConnect()
        cur.execute(sql)
        print('开始执行【删除】mysql语句:%s'%sql)
        self.conn.commit()
        self.conn.close()

    def dropMysqlData(self,table):
        '''删除表本身，即表中数据和表结构（列、约束、视图、键）全部删除'''
        cur = self.__GetConnect()
        cur.execute('drop table %s'% table)
        print('开始执行【删除】mysql语句:%s'%sql)
        self.conn.commit()
        self.conn.close()



if __name__ == '__main__':
    m = MysqlCmd('127.0.0.1',3306,'root','123456','test')
    tlist=['t1','t2']
    m.tranckMysqlData(2,tlist)
    sql = "insert into t1(id,name) values(4,'kk')"
    # m.insertMysqlData(sql)
    sql = "update t1 set name='yu' where id=1"
    m.updateMysqlData(sql)
    sql = 'select id,name FROM t1'
    r = m.queryMysqlDatas(sql)
    print(r)