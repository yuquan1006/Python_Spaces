#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 18:06
# @Author  : Yuquan
# @Site    :
# @File    : deMo.py
# @Software: PyCharm

# xx
for i in range(1, 91):
    for j in range(1, 91):
        for k in range(1, 91):
            if i+j+k == 90 and 3*i+2*j+0.5*k == 90:
                print(i, j, k)

# 一行代码实现1-100的和
print(sum([x for x in range(1, 101)]))  # 列表推导式
print(sum((x for x in range(1, 101))))  # 生成器表达式

# python 标准库：
import unittest,os,time,datetime,sys,json,re,math,random

# 10个liunx命令
# tail , find ,vi ,ps ,top, netstat, rm,mv,tar,cat,cd,ll,pwd,scp,ssh,sh,

# open 函数中r/r+/rb/rb+的区别 r普通读文件，rb 二进制方式读文件 r+为可读写两种操作

# 数组和元祖的区别： 元祖的值不可改变。

#迭代器：实现了_iter_方法和_next_方法的类对象，就是迭代器

# 生成器：生成器是一种特殊的迭代器.这种一边循环一边计算的机制，称为生成器. 优点:节省cpu和内存
# 1 生成器函数:使用 def 定义函数，但是，使用yield而不是return语句返回结果

# 2 生成器表达式:类似于列表推导，只不过是把一对大括号[]变换为一对小括号()。但是，生成器表达式是按需产生一个生成器结果对象，要想拿到每一个元素，就需要循环遍历
print(sum((x for x in range(1, 101))))  # 生成器表达式


# cookes：Cookies是服务器在本地机器上存储的小段文本并随每一个请求发送至同一服务器，是在客户端保持状态的方案
# session:存在服务器的一种用来存放用户数据的类HashTable结构。

# cookies 和session的关连：ession的实现方式和Cookie有一定关系。建立一个连接就生成一个session id，打开几个页面就好几个了，这里就用到了Cookie，
# 把session id存在Cookie中，每次访问的时候将Session id带过去就可以识别了.

# session和cookies区别：
# 存储数据量方面：session 能够存储任意的 java 对象，cookie 只能存储 String 类型的对象
# 一个在客户端一个在服务端。因Cookie在客户端所以可以编辑伪造，不是十分安全。
# Session过多时会消耗服务器资源，大型网站会有专门Session服务器，Cookie存在客户端没问题。
# 域的支持范围不一样，比方说a.com的Cookie在a.com下都能用，而www.a.com的Session在api.a.com下都不能用，解决这个问题的办法是JSONP或者跨域资源共享。


# 猜拳游戏
import random
def caiquan():
    temp = False
    while not temp:
        try:
            per = int(input("请输入你的选择（0-石头,1-剪刀,2-步）"))
            if isinstance(per, int) == True:
                temp = check_result(per)
            else:
                print("错误！你输入的非数字！")
        except:
            print("包含其他字符，请重新输入")
def check_result(user):
    if 0 <= user <= 2:
        com = random.randint(0, 2)
        dict = {0: "石头", 1: "剪刀", 2: "步"}
        if user == 0 and com == 1 or user == 1 and com == 2 or user == 2 and com == 0:
            print("你出的是%s 电脑出的是：%s 恭喜你胜利！" % (dict[user], dict[com]))
            return True
        elif user == 0 and com == 0 or user == 1 and com == 1 or user == 3 and com == 3:

            print("你出的是%s 电脑出的是：%s  你和电脑打平了" % (dict[user], dict[com]))
            return True
        else:
            print("你出的是%s 电脑出的是：%s  你输给电脑了！ " % (dict[user], dict[com]))
            return True

    else:
        print("你输入数错误,（0-石头,1-剪刀,2-步）:")
        return False
# caiquan()


# eval 将字符串str当成有效的表达式来求值并返回计算结果
# 整形，列表，元祖，字典都可以
a = '123'
a = type(eval(a))
# 列表字符串转化成列表
b = "[2, 44, \"ff \"]"
b = type(eval(b))
# print(b)
# eval 实现计算器
def calc():
    value = input("请输入算术题（1+5）")
    return  eval(value)
# print(calc())


# 利用内置函数chr(),ord()以及random模块写一个简单随机4位验证码
def createCode():
    temp = ''
    for i in range(0, 4):
        n = random.randint(0, 1)
        if n == 0:
            value = random.randint(65, 121)
            temp = temp+chr(value)
        else:
            value = random.randint(0, 9)
            temp = temp+str(value)
    print(temp)
createCode()

# 实现用户输入用户名和密码，当用户名为 seven且密码为123时，显示登陆成功，否则登陆失败，失败时允许重复输入三次

def login():
    i = 0
    while True:
        username = input("输入用户名:\n")
        passwd = input("输入密码:\n")

        if username == "yuquan" and passwd == "123":
            print("登录成功！")
            break
        else:
            i += 1
            print("登录失败！还有%s机会" % str(4-i))
            if i == 4:
                print("登录次数用完了！ 请稍后再试！")
                exit()
            else:
                continue

# chandao()

# 使用while循环实现输出2-3+4-5+6.....+100的和
def calc01():
    num = 2
    sum = ''
    while num <= 100:
        if num % 2 == 0 :
            sum = sum + str(num)+"-"
        else:
            sum = sum + str(num)+"+"
        # print(sum)
        num+=1
    print(eval(sum[:-1]))
# calc01()
# print('12345'[:-1])
def calc02():
    sum = 0
    for i in range(2, 101):
        if i % 2 == 0:
            sum += i
        else:
            sum -= i
        print(i,sum)
    print(sum)
# calc02()



import xlrd,xlwt
def writeExcel():
    with open(r"C:\Users\A\Desktop\t.txt") as f:
        a = f.read()
        print(a)
        b = json.loads(a)
        print(b)
        # b = sorted(b.items(), key = lambda items: items[0], reverse=False)
        print(b)
    d1 = []
    for i, j in b.items():
        d = []
        d.append(i)
        for k in j:
            d.append(k)
        d1.append(d)
    print(d1)
    work = xlwt.Workbook(encoding='utf-8')
    sheet = work.add_sheet('test', cell_overwrite_ok=True)
    for n1, i in enumerate(d1):
        for n2, j in enumerate(i):
            sheet.write(n1, n2, j)
    work.save(r"C:\Users\A\Desktop\t.xls")

'''
斯蒂芬和索菲亚对于一切都使用简单的密码，忘记了安全性。请你帮助尼古拉开发一个密码安全检查模块

如果密码的长度大于或等于10个符号，至少有一个数字，一个大写字母和一个小写字母，该密码将被视为足够强大
密码只包含ASCII拉丁字母或数字
输入: 密码 (str, unicode)
输出: 密码的安全与否，作为布尔值(bool)，或者任何可以转换和处理为布尔值的数据类型。你会在结果看到转换后的结果(True 或 False)
'''
a= ''

import re
def check(passwd):
    return ( (len(passwd) >= 10) and     #长度大于等于10
            (not passwd.islower()) and  # 不都是小写  （有大写）
            (not passwd.isupper()) and   # 不都是大写 （有小写）
            (not passwd.isalpha()) and   #不都是字母（有数字）
            (not passwd.isdigit()) and   # 不都是数字（有字母）
             (passwd.isalnum()))          # 只是数字和字母

print(check('125ff5'))

'''
动态参数*arg和**kwargs 
*args：是指当我们需要传入多个参数时，可以用*args代表多个参数，不用分别在括号里指定多个参数。它将传入的参数放在一个元祖中
 **kwargs,：当我们需要传入键值对类型的参数时就可以用**kwargs。它将穿入的键值对放在一个字典中

'''
def test(*args, **kwargs):
    print(args)
    print(kwargs)
    print("我的名字：{a} 我的年龄：{b}".format(a=args[0], b = args[1]))
    print("我喜欢：{c} 我不喜欢：{e}".format(c = kwargs.get('like'),e = kwargs.get('nlike')))
test('yuquan',12,like='汽水',nlike='试试')


a = {"k":12, "kk":22}
if a.get('k3') == None:
    print('y')
else:
    print('n')

# --统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
a = [1, 3, 5, -7, 0, -1, -9, -4, -5, 8]
b = [x for x in a if x>0]
c = [x for x in a if x<0]
print(len(b), len(c))

# 字符串 "axbyczdj"，如果得到结果“abcd”
a = "axbyczdj"
a = a[::2]
print(a)



# 1.遍历查找文件夹内所有的子文件（不包含文件夹）,查找后置是.py结尾的
import os
path = r"C:\Users\A\Desktop"
a = os.listdir(path) # 返回指定的路径下包含的文件或文件夹的名字的列表
result = []
print(a)
for i in a:
    if i.endswith(".py"):
        result.append(i)
print(result)

a = os.walk(path,topdown=True)      ## 通过在目录树种游走输出在目录中的文件名，向上或者向下
result = []
for dirpath,dirnames,filenames in a:
    # print(filenames)
    for i in filenames:
        if i.endswith(".py"):
            result.append(i)

print(result)


# 下面一个例子，假设三个人打牌，首先要保证54张牌没有重复的，第人发手里18张（斗地主就不能平均分配了）
from pprint import *                                    # 调用pprint 模块
# values = list(range(1,13)) + "dwang xwang".split()   # 定义13个数字与大小王   # p3 和p2中range返回值变了 在3要加list（range（x，x1））才返回列表
# print(values)
# color = 'hei hong mei fang'.split()                    # 定义四中花色
# huen = ['%s of %s' %(v,s) for v in values for s in color ]      # 循环嵌套将其循环组合
# pprint(huen[:10])                                                  # 可输出python所有数据类型
# print('--------------------------------')
# # 以上输出的不够乱  就用random下shuffle模块  原地指定序列
# from random import shuffle
# shuffle(huen)
# pprint(huen[:18])


# sys模块
import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)


# 数据的可变与不可变   数字数据类型是不允许改变的,这就意味着如果改变数字数据类型的值，将重新分配内存空间
i = 12
i2 = i
print(i,i2)
i = 'naem'
print(i)

list = ['a',23,32]
print(list[0])
list[0] = 12
print(list[0])



# is 身份运算符用于比较两个对象的存储单元   is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
age2 = 10
age = 10
if (age2 is age):
    print('yiyang')
else:
    print('wom buyiy')

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名
#  a = abs # 变量a指向abs函数
#  a(-1) # 所以也可以通过a调用abs函数



#
# 冒泡排序 原理：每轮只能将一个数归位，如果有n的个数，就要将n-1个数归位
# list = [1,40,20,30]
# for i in range(len(list)-1):            # 确定循环的轮数，比如四个数就要三轮，每轮确定一个最大数。
#     for j in range(len(list)-i-1):      # 每轮循环需要比较的次数 比如 list = [1,40,20,30] 需要比较3次
#         if list[j] >list[j+1]:
#             list[j],list[j+1] = list[j+1],list[j]
# print(list)
#
# 选择排序
# 1. 选择一个基准球2. 将基准球和余下的球进行一一比较，如果比基准球小，则进行交换3. 第一轮过后获得最小的球　　
# list = [60,30,20,40]
# # for i in range(len(list)-1):            # 确定循环的轮数，比如四个数就要三轮，每轮确定一个最小数。
# #     index = i                           # 从0比较n-1 index为基准球位置下标
# #     for j in range(i+1,len(list)):      #　用index的值分别与后面的值进行比较,以便获取最小index
# #         if list[index]>list[j]:         #　如果找到比当前值小的index,则进行两值交换
# #             list[index],list[j] = list[j],list[index]

a = [0,1,2,3,4,5,6]
print(a)
print(a[1::2])
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(value):
    if not isinstance(value,str):
        print('输入参数类型错误')
        raise ValueError
    return to_no(value)

def to_no(value):
    while  value[0] == " " or value[-1] == " ":
        if value[0] == " ":
            value = value[1::]
        if value[-1] == " ":
            value = value[:-1]
        print(value)
    return value


print(len(to_no(' 124 ' )))

