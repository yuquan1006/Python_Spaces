#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 16:25
# @Author  : Yuquan
# @Site    : 
# @File    : 函数编程+闭包+回调.py
# @Software: PyCharm
# 闭包函数和回调函数

# ------------------闭包
def func_01():
    name = '余泉外部'
    # 如果在一个内部函数里， 对在外部作用域（但不是在全局作用域） 的变量进行引用， 那么内部函数就被认为是闭包
    def func_02():
        # print(name)
        return name.replace('外部','内部')
    return func_02


# -------------------回调：通过函数参数传递到其他代码的，某一块可用执行代码的应用。
def callback(input):
    print("function my_callback was called with %s input" % (input))


def call(input,func):
    func(input)


# 函数式编程：函数本身可以赋值给变量，赋值后变量为函数； 允许将函数本身作为参数传入另一个函数； 允许返回一个函数。
def print_01():
    print('hello world')
hello = print_01

def reset_data(a=0):
    a = 1
    return a
def add(func1,num):
    return func1+num

def return_func(func):
    return func

if __name__ == '__main__':
    print(func_01()())
    callback('s')
    call(1,callback)
    hello()
    print(add(reset_data(1),2))
    print(return_func(reset_data()))