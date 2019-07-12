#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# @Version : 1.0  
# @Time    : 2018/4/14  
# @Author  : YUQUAN
# 学习重点 if、while、for和函数

# 斐波纳契数列 1,1,2,3,5,8.....
# def printFibo(num):
#
#     a = 0
#     b = 1
#     i = 0
#
#     while i < num:
#         print(a,end=',')
#         a,b = b, a+b
#         i += 1
#
# printFibo(20\n)


# 控制流 - if
# 猜数字
anwwer = 22
uesr = int(input('请输入你的答案:'))

if anwwer == uesr:
    print('恭喜你！ 猜对了')
elif anwwer < uesr:
    print("抱歉，你猜的大了一下")
else:
    print("抱歉，你的猜的小了一些")

print('done')
#
#
# name = '余泉'
# uesrname = input("你知道小羊最喜欢谁")
# if name == username:
#     print("恭喜你猜对了，是余泉哦")
# else:
#     print("no,你猜错了")



#
# # while 循环
# num = 30
# running = True
# count = 0
#
#
# while running:
#     anwser = int(input('请输入你的答案：'))
#     count+=1
#     if num == anwser:
#         print('恭喜你！ 猜对了')
#         break                   # break 语句来中断循环
#         # running = False
#     elif num > anwser:
#         print("抱歉，你的猜的小了一些")
#         if count >= 3:
#             running = False
#             print("抱歉，机会已经用完了")
#     else:
#         print("抱歉，你猜的大了一下")
#         if count >= 3:
#             running = False
#             print("抱歉，机会已经用完了")
# else:
#     print('循环终止了')          # else 代码块在 while 循环的条件变为 False 时开始执行  只要循环里出现了break 就不会执行else



# for 循环 1-100 累加
# sum = 0
# i = 1
#
# for i in  range(1,100):       # range 函数生成这一数字序列 range(1,4) 生成1,2,3 默认是++
#     sum = i + sum
#
# else:
#     print(sum)
#
# list = [2,'china','america','english']
# for i in list:
#     if i == 'china':
#         print('china no1')
#         break
#     print(i)
# else:
#     print('结束')



# break语句用以中断循环语句，也就是中止循环语句的执行，即使循环条件没有变更为 False ，或队列中的项目尚未完全迭代依旧如此。
# tips： 如果你的 中断 了一个 for 或 while 循环，任何相应循环中的else 块都将不会被执行
# running = True
# while running:
#     some = input('输入你的姓名：')
#     if some == '小羊':
#         print('真爱',)
#         running = False
#     print(some,len(some))
# else: print('循环结束')


#  continue 语句用以告诉 Python 跳过当前循环块中的剩余语句，并继续该循环的下一次迭代。

# while True:
#     s = input('Enter something : ')
#     if s == 'quit':
#         break
#     if len(s) < 4:
#         print('Too small')
#         continue  # 跳过当前循环剩余语句，开始下一次迭代
#     print('Input is of sufficient length')


# 函数  关键字：def
# def sayhello():
#     print('hello')
# def addnum(a,b):
#     return str(a+b)    # 转换下
# def print_max(a,b):
#     if a>b:
#         print('a>b,a是最大叔')
#     elif a == b:
#         print('a=b,无最大数')
#     else:
#         print('a<b,b是最大数')
# print_max(3,0)

# x = 90
# def func(x):     # 当你在一个函数的定义中声明变量时，它们不会以任何方式与身处函数之外但具有相同名称的变量产生关系，也就是说，这些变量名只存在于函数这一局部（Local）
#                 # 。这被称为变量的作用域（Scope）。所有变量的作用域是它们被定义的块，从定义它们的名字的定义点开始
#
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)
# func(x)
# print('x is still',x)


# some = input('打个招呼吧！\n')
# if some == 'hello':
#     sayhello()
#  shu = int(input('请输入一个数'))
#  shu2 = int(input('请再输入一个数'))
#  print('两数之和是：'+addnum(shu,shu2))

# global 如果你想给一个在程序顶层的变量赋值（也就是说它不存在于任何作用域中，无论是函数还是类），那么你必须告诉 Python 这一变量并非局部的，而是全局（Global）的。我们需要通
# 过 global 语句来完成这件事
# x = 100
# def func():
#     global x    # x定义了全局变量，所以在函数内修改x的值在全局都可以起到作用
#     print('x=',x)
#     x = 12
#     print('change x',x)
# func()
# print('finnal x =',x)

#  函数默认值参数  可以通过在函数定义时附加一个赋值运算符（ = ）来为参数指定默认参数值
# def say(message,times = 2):
#     print(message * times)
# say('i love you  ')
# say('hello  ',6)

# 函数不定长参数
# def printinfo(arg1, *vartuple):
#     # "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return;
# # 调用printinfo 函数
# printinfo(10);
# printinfo(70, 60, 50);

# 函数关键字参数
# def printme(str):   # str为关键字
#     "打印任何传入的字符串"
#     print(str);
#     return;
# # 调用printme函数
# printme(str='hello')
#
# def printinfo(name, age=18):   # 函数参数的使用不需要使用指定顺序
#     # "打印任何传入的字符串"
#     print("名字: ", name);
#     print("年龄: ", age);
#     return;
# # 调用printinfo函数
# printinfo(age=20,name="runoob");


# return 语句用于从函数中返回，也就是中断函数。我们也可以选择在中断函数时从函数中返回一个值
# def maxnum(a,b):
#     if a > b:
#         return a
#     elif a == b:
#         pass # pass语句用于指示一个没有内容的语句块,返回none
#     else:
#         return b
# print(maxnum(7,7))

# 文档字符串  文档字符串所约定的是一串多行字符串，其中第一行以某一大写字母开始，以句号结束。 第二行为空行，后跟的第三行开始是任何详细的解释说明
# def down(a,b):
#     '''Down 相当于减法运算
#
#     要求减数要比被减数的值大.'''
#     return a-b
# print(down(12,4))
# # help(down)   # help+函数名即可查看函数的属性
# # print(max.__doc__)  #函数名.__doc__ 可查看函数的属性


