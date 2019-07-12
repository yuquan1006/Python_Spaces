#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 16:57
# @Author  : Yuquan
# @Site    : 
# @File    : 装饰器.py
# @Software: PyCharm
import time
import functools
# 装饰器

def run_time(func):
    @functools.wraps(func) # 原始函数的__name__等属性复制到wrapper()函数中 比如 func函数的属性给到warpper函数
    def wrapper():
        print('开始运行内部函数---------')
        starttime = time.time()
        print(starttime)
        func()
        endtime = time.time()
        print(endtime)
        print('运行完毕,运行时间为:%s---------' % str(endtime-starttime))

    return wrapper

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("调用%s函数"%func.__name__)
        result = func(*args,**kwargs)
        print("调用完成!")
        return result
    return wrapper

@log
def func_01(a,b):
    print("python程序！参数为%s,%s"%(a,b))
    time.sleep(2)

# 本质 func_01 = log(func_01)

@run_time
def func():
    print('我是一个输出hello world 的简单函数')
    time.sleep(1)
# 本质 func = log(func)

def log_01(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print("调用%s函数,且传入自定义文本%s"%(func.__name__,text))
            result = func(*args,**kwargs)
            print("调用完成!")
            return result
        return wrapper
    return decorator

# 本质 func_02 = log_01(’中国‘)(func)
@log_01('中国')
def func_02():
    print('hello world!')




if __name__ == '__main__':
    func_02()
