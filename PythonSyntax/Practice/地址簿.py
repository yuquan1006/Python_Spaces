#!/usr/bin/env python
# encoding: utf-8
# author: 余泉
# version: python3.6
# file: 地址簿.py
# time: 2018\4\20 0020 8:46
'''
pickle 中的load、dump方法是对文件读取、存储     对象持久化
pickle 中的loads、dumps方法是对变量读取、存储
'''
# 调试文件
import pickle
import os
import sys
path = 'abc.data'
class Person:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

def updata():
    s = input("请输入类似于jack,jack@ict.ac.cn,13543454567:")
    p_list = s.split(",")
    f = open(path, "rb")
    content = pickle.load(f)
    content[p_list[0]] =p_list[1]+','+p_list[2]
    f =open(path, 'wb')
    pickle.dump(content, f)
    f.close()
    del content


def select():
    f = open(path, "rb")
    content = pickle.load(f)
    print(content)
    name = input("请输入查询人的姓名：")
    if name not in content.keys():
        print("你输入的姓名有误！重新输入：")
    else:
        print("你查询%s的信息为：" %name+':'+content[name])

def delete():
    f =open(path,"rb")
    content = pickle.load(f)
    print(content)
    name = input("请输入你要删除的姓名：")
    if name in content.keys():
        del content[name]
        f =open(path,'wb')
        pickle.dump(content,f)
        del content
    else:
        print("你输入的姓名有误！重新输入：")

def exit():
    sys.exit()

def main():
    while True:
        meu = input(''''' 
                        1.查询 
                        2.添加/修改 
                        3.删除 
                        4.退出 
                        ------>''')

        if meu == "1":
            select()
        elif meu == "2":
            updata()
        elif meu == '3':
            delete()
        elif meu == '4':
            exit()
        else:
            print("输入参数有误！")

if __name__ == '__main__':
    if os.path.exists('abc.data'):
        main()
    else:
        f = open('abc.data', 'wb')
        conlist = {'jack': 'jack@ict.ac.cn,13645654345'}
        pickle.dump(conlist, f)
        f.close()
        del conlist
        main()

