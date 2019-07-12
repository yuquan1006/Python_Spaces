#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 13:23
# @Author  : Yuquan
# @Site    : 
# @File    : python设计模式_单例.py
# @Software: PyCharm

# 方法一：用__new__实现，将类实例绑定到类变量_instance上面
# 如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回
# 如果cls._instance不为None,直接返回cls._instance
# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not (hasattr(cls, '_instance')):  # hasattr() 返回对象是否具有具有给定名称的属性。
#             orig = super(Singleton, cls)
#             cls._instance = orig.__new__(cls, *args, **kwargs)
#         return cls._instance




# 2.装饰器实现
def singleton(cls ):
    _instance = {}
    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return _singleton
@singleton
class MyClass4(object):
    a = 1
    def __init__(self, x=0):
        self.x = x

if __name__ == '__main__':
    # s = Singleton()
    # s1 = Singleton()
    # print(id(s1))
    # print(id(s))
    a = MyClass4()
    b = MyClass4()
    print(id(a))
    print(id(b))