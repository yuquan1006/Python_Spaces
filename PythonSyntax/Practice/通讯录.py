#!/usr/bin/env python
# encoding: utf-8
# author: 余泉
# version: python3.6
# file: 通讯录.py
# time: 2018\7\5 0005 19:18

# f = open('test.txt', 'a')
# # str通过encode()方法可以编码为指定的bytes 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
# f.write('idddd')
# f.close()
#
# f = open('./test.txt', 'r')
# print(f.readline())
# f.close()
import os
# print(os.path.split(os.path.realpath(__file__))[0])

# 文件备份
# def copy_file(old_path):
#     new_path = os.path.split(old_path)[0]
#     fname = os.path.split(old_path)[1]
#     num = fname.find('.')
#     new_filename =os.path.join(new_path,fname[:num]+'_copy'+fname[num:])
#
#     f = open(old_path,'rb')
#     content = f.read().decode()
#     f.close()
#     f = open(new_filename,'wb')
#     f.write(content.encode())
#     f.close()
# copy_file(r'C:\Users\Administrator\PycharmProjects\Python_base\PythonBase\demo2\test.txt')
# f = open('test.txt','rb')
# content = f.read(10).decode()
# print(content)
# print(f.tell())
# print(f.seek(0,1))
# print(f.tell())
# # 读取一个文件，显示除了以井号(  # )开头的行以外的所有行
# f = open('test.txt','rb')
# if f.readline().decode()[0] == '#':
#     print(f.read().decode())
# else:
#     f.seek(0,0)
#     print(f.read().decode())

# 制作一个"密码薄",其可以存储一个网址（例如 www.itcast.cn），和一个密码(例如 123456)，请编写程序完成这个“密码薄”的增删改查功能，并且实现文件存储功能
# 用来存储名片
import pymysql
card_infors = []
path = r"C:\Users\A\Desktop\test.txt"
def  login(func):
    '''为该系统添加登录验证功能'''
    def login_pandui():
        while True:
            username = input('输入用户名: ')
            password = input('输入密码: ')
            try:
                cursor = pymysql.connect( host='localhost',port=3306, user='root',passwd='root',db='mysql',charset='utf8').cursor()
                cursor.execute("select username,passwd from demo")
                users = cursor.fetchall()
            except:
                print('连接数据库失败')
            finally:
                cursor.close()

            a,b =[],[]
            for user in users:
               a.append(user[0])
               b.append(user[1])
            if username in a and password in b:
                    print('登录成功!')
                    break
            else:
                print('用户名或者密码错误！')
                print('请重新输入')
        func()
    return login_pandui

# @login
def print_menu():
    """完成打印功能菜单"""
    print("=" * 50)
    print("   名片管理系统 V0.01")
    print(" 1. 添加一个新的名片")
    print(" 2. 删除一个名片")
    print(" 3. 修改一个名片")
    print(" 4. 查询一个名片")
    print(" 5. 显示所有的名片")
    print(" 6. 保存信息")
    print(" 7. 退出系统")
    print("=" * 50)


def add_new_card_infor():
    """完成添加一个新的名片"""
    new_name = input("请输入新的名字:")
    new_qq = input("请输入新的QQ:")
    new_weixin = input("请输入新的微信:")
    new_addr = input("请输入新的住址:")

    # 定义一个新的字典,用来存储一个新的名片
    new_infor = {}
    new_infor['name'] = new_name
    new_infor['qq'] = new_qq
    new_infor['weixin'] = new_weixin
    new_infor['addr'] = new_addr

    # 将一个字典,添加到列表中
    global card_infors
    card_infors.append(new_infor)
    print("添加成功！")
    # print(card_infors)# for test


def find_card_infor():
    """用来查询一个名片"""

    global card_infors

    find_name = input("请输入要查找的姓名:")
    find_flag = 0  # 默认表示没有找到
    for temp in card_infors:
        if find_name == temp["name"]:
            print("查询成功！")
            print("%s\t%s\t%s\t%s" % (temp['name'], temp['qq'], temp['weixin'], temp['addr']))
            find_flag = 1  # 表示找到了

            break

    # 判断是否找到了
    if find_flag == 0:
        print("查无此人....")


def show_all_infor():
    """显示所有的名片信息"""

    global card_infors
    print("姓名\tQQ\t微信\t住址")
    for temp in card_infors:
        print("%s\t%s\t%s\t%s" % (temp['name'], temp['qq'], temp['weixin'], temp['addr']))


def save_2_file():
    """把已经添加的信息保存到文件中"""
    try:
        f = open(path, "w")

        f.write(str(card_infors))


    except BaseException as e:
        print("信息保存失败！%s" %e)
    else:
        print('新增信息保存成功！')
    finally:
        f.close()

def load_infor():
    global card_infors

    try:
        f = open(path)

        card_infors = eval(f.read())

        f.close()
    except Exception:
        pass

import pymysql.cursors as cursors


def main():
    """完成对整个程序的控制"""

    # 恢复(加载)之前的数据到程序中
    load_infor()

    # 1. 打印功能提示
    print_menu()

    while True:

        # 2. 获取用户的输入
        num = int(input("请输入操作序号:"))

        # 3. 根据用户的数据执行相应的功能
        if num == 1:
            add_new_card_infor()
            print_menu()

        elif num == 2:
            pass
        elif num == 3:
            pass
        elif num == 4:
            find_card_infor()
            print_menu()

        elif num == 5:
            show_all_infor()
            print_menu()

        elif num == 6:
            save_2_file()
            print_menu()

        elif num == 7:
            break
        else:
            print("输入有误,请重新输入")
            print_menu()

        print("")


if __name__ == "__main__":
    # 调用主函数
    main()

