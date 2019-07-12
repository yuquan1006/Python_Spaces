#!/usr/bin/python
#author         :YUQUAN
#projectName    :huice_base
#date           :
#version        :PYTHON3.6
#File           :python_100.py
# 20 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
# start = 100
# time = 10
# juli = []
# gao = []
# for i in range(1,time+1):
#     if i == 1:
#         juli.append(start)
#     else:
#         juli.append(start*2)
#     start = start / 2
#     gao.append(start)
# print(sum(list))
# print(gao[-1])

# 21 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃
# 了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
# 10 4
# 9 10
# 8 22
# x = 1
# for day in range(9,0,-1):
#     ge = (x+1)*2
#     x = ge
#
# print(ge)
# 22 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比
# ，c说他不和x,z比，请编程序找出三队赛手的名单。


# # 2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
# a = 1
# b = 2
# sum = 0
# for i in range(1,21):
#     print(str(b) + '/' + str(a))
#     sum = sum + b / a
#     a,b=b,a+b
# print(sum)


# 25 求1+2!+3!+...+20!的和。
# n =1
# list =[]
# for i in range(1,21):
#     n  = n*i
#     list.append(n)
# print(sum(list))

# 27 用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来
# def output(s,l):
#     if l == 0:
#         return
#     else:
#         print(s[-1],end='')
#         output(s,l-1)
# s = input(':')
# l = len(s)
# output(s,l)

# 利用递归方法求5!。
# def fan(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fan(n-1)
# print(fan(5))

# 用递归算法来求斐波拉契数列 1，1，2,3,5,8
# def fib_list(n) :
#   if n == 1 or n == 2 :
#     return 1
#   else :
#     m = fib_list(n - 1) + fib_list(n - 2)
#     return m
# print("**********请输入要打印的斐波拉契数列项数n的值***********")
# n = int(input('enter:'))
# list = [0]
# ten = 1
# while n>=ten:
#     list.append(fib_list(ten))
#     ten+=1
# print(list)


# 有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人
# ，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
# def age(n):
#     if n == 1:
#         c = 10
#     else:
#         c = age(n-1)+2
#     return c
# print(age(3))

# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
num = int(input(';'))
ge = num % 10
shiwei = num % 100 // 10
baiwei = num % 1000 // 100
qian = num % 10000 // 1000
wang = num / 10000

if 1 < num / 10000 < 10:
    print('is 5 \n',ge,shiwei,baiwei,qian,wang)
if 1 < num / 1000 < 10:
    print('is 4\n', ge,shiwei,baiwei,qian)
if 1 < num / 100 < 10:
    print('is 3\n', ge,shiwei,baiwei )
if 1 < num / 10 < 10:
    print('is 2\n',ge,shiwei)
if 1 < num / 1 < 10:
    print( 'is 1\n',ge)


#   第二种解法
# x = int(input("请输入一个数:\n"))
# a = x / 10000
# b = x % 10000 // 1000
# c = x % 1000 // 100
# d = x % 100 // 10
# e = x % 10
# print(c)
#
# if a > 1:
#     print("5 位数：", e, d, c, b, a)
# elif b != 0:
#     print("4 位数：", e, d, c, b,)
# elif c != 0:
#     print("3 位数：", e, d, c)
# elif d != 0:
#     print("2 位数：", e, d)
# else:
#     print("1 位数：", e)
