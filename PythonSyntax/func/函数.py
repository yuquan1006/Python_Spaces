#!/usr/bin/env python
# encoding: utf-8
# author: 余泉
# version: python3.6
# file: 函数.py
# time: 2018\7\5 0005 11:11

# 定义一个函数，能够输出自己的姓名和年龄，并且调用这个函数让它执行
# def print_info(name,age):
#     '''
#      文档说明：打印姓名和年龄
#     :param name:
#     :param age:
#     :return:
#     '''
#     print('你的姓名是:{}  年龄是:{}'.format(name,age))
#
# print_info('余泉', 25)
# print(print_info.__doc__)

# 定义一个函数，完成前2个数完成加法运算，然后对第3个数，进行减法；然后调用这个函数
# def calc(a,b,c):
#     '''
#     完成前2个数完成加法运算，然后对第3个数，进行减法
#     :param a:
#     :param b:
#     :param c:
#     :return:
#     '''
#     sum = (a+b)-c
#     return sum
# print(calc(1,3,2))

# def printOneLine():
#     print("-"*30)
#
# # 打印多条横线
# def printNumLine(num):
#     for i in range(num):
#         printOneLine()

# printNumLine(4)
# 写一个函数求三个数的和
# 写一个函数求三个数的平均值
# def sum(a,b,c):
#     return a+b+c
#
# def avg(a,b,c):
#     return sum(a,b,c)//3
# print(avg(5,5,11))
# a = 10
# list = []
# def test():
#     list=[1,2]
#     print('tes函数中a变量的值', list)
# def test1():
#     global a
#     list=[1,55]
#     print('test1函数中a变量的值',a)
# def test2():
#     list = [0]
#     c = 22
#     print(list)
#     return a,list,c
# test()
# test1()
# # print(test2())
#
def fun(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
fun(1,2,3,4,p=2,w='yi')
c = (3,4,5)
d = {'username': 125, 'passwd': 125552}
fun(1,2,*c,**d)
# 函数参数传递
# def func(val):
#     val.append(100)     # 无重新赋值的话 val和L都指向同一个对象
#     val = ['x','y', 'z']    #  重新赋值后val指向['x','y', 'z']对象了
#     return val
#
# L = [1, 10]
# print(func(L))
# print(L)

# 因为list是可变数据类型，内存地址不会变，当list1掉用函数是默认参数空列表+10，内存列表为[10]
# def extendList(val,list=[]):
#     list.append(val)
#     return list
#
# list1=extendList(10)
# print(list1)
# list2=extendList(1234,[])
# print(list2)
# list3=extendList('abc')
# print(list3)
# 递归函数实现阶乘
# n! = 1 * 2 * 3 * ... * n
# def fn(num):
#     if num == 1:
#         return 1
#     return fn(num-1)*num
# print(fn(5))

# def fn(num):
#     sum = 1
#     for i in range(2,num+1):
#         sum = i*sum
#     return sum
# print(fn(4))
#
# def fn(num):
#     i=1
#     sum=1
#     while i<=num:
#         sum = i*sum
#         i+=1
#     return sum
# print(fn(5))

# fn = lambda a,b:a+b
# print(fn(1,2))
# def add(a,b,opt):
#     return opt(a,b)
# print(add(2,3,lambda a,b:a+b))
# stus = [
#     {"name":"zhangsan", "age":18},
#     {"name":"lisi", "age":19},
#     {"name":"wangwu", "age":17}
# ]   # 安装年龄排序
# a = sorted(stus,key=lambda a:a['age'],reverse=True)
# print(a)
# # 按照姓名排序 ASSIC排序
# stus.sort(key=lambda x:x['name'],reverse=True)
# print(stus)

# 编程实现 9*9乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{j}*{i}={s}  '.format(j=j,i=i,s=i*j),end='')
#     print('\n')
# i=1
# while i<10:
#     j =1
#     while i>=j:
#         print('{j}*{i}={s}  '.format(j=j, i=i, s=i * j), end='')
#         j+=1
#     print('\n')
#     i+=1

# 用函数实现求100-200里面所有的素数
# def test(a,b):
#     lists=[]
#     for i in range(a,b):
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             lists.append(i)
#     return lists
# print(test(1,100))

# def run():
#     year = int(input('请输入:'))
#     if (year % 4==0 and year % 100 !=0) or year%400 ==0:
#         print(year)
#     else:
#         print('不是闰年')
#
# run()
# 函数实现输入某年某月某日，判断这一天是这一年的第几天？闰年情况也考虑进去
# 2018-05-05
# def dateFun(lists):
#     lists = str(lists)
#     if len(lists)==8:
#         year = int(lists[0:4])
#         month = int(lists[4:6])
#         day = int(lists[6:])
#
#         days = [0,31,59,90,120,151]
#         tian = days[int(month)-1]+int(day)
#         if year%4==0 and year%100 !=0 or year%400 ==0:
#             result =tian+1
#             print('{}是今年第{}天'.format(lists, result))
#         else:
#             result =tian
#             print('{}是今年第{}天'.format(lists,result))
# dateFun(20180503)

a=1
g={'a':22}

print(a)
print(eval("a+1",g))