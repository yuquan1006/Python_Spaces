#!/usr/bin/env python
# encoding: utf-8
# author: 余泉
# version: python3.6
# file: 面向对象二.py
# time: 2018\7\9 0009 19:23

# 写一个雷锋类，定义买米和扫地两个方法，写一个学生类和社区志愿者类，继承雷锋类，写一个工厂类，根据输入的类型返回学生类或志愿者类。
# 工厂设计模式 雷锋类，大学生类，志愿者类和简单工厂一样，新写一个工厂方法基类，定义一个工厂方法接口（工厂方法模式的工厂方法应该就是指这个方法），然后写一个学生工厂类，志愿者工厂类，重新工厂方法，
# 返回各自的类
class Leifeng:
    def by_mi(self):
        pass
    def sweep(self):
        pass


class Stu(Leifeng):
    def by_mi(self):
        print('大学生买米')

class Zhiyuan(Leifeng):
    def by_mi(self):
        print('志愿者买米')
# 简单工厂
# class LeifengFactory:
#     def create(self,type):
#         if type == '大学生':
#             return Stu()
#         elif type == '志愿者':
#             return Zhiyuan()
# p = Factory().create('大学生')
# p.by_mi()
class LeifengFactory:
    def create_leifeng(self):
        pass
class Stu_Factory(LeifengFactory):
    def create_leifeng(self):
        return Stu()
class Zhiyuan_Factory(LeifengFactory):
    def create_leifeng(self):
        return Zhiyuan()

# P =Stu_Factory().create()
# P.by_mi()
# P = Zhiyuan_Factory().create()
# P.by_mi()


# __new__ 和 __init__

class B:
    def test(self):
        print('本身函数')
class A(B):
    # 初始化函数
    def __init__(self):
        print('初始化函数__init__被调用')

    # _new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
    def __new__(cls):
        print('这是new实例化出实例方法')
        # __new__必须有返回值。返回实例化出来的实例  return父类__new__出来的实例，或者直接是object的__new__出来的实例
        return B.__new__(cls)
        return object.__new__(cls)
    def test(self):
        print('本身函数')
# a= A()
# a.test()

# class Singleton(object):
#     # 定义保护变量instance（实例）为none
#     __instance = None
#     __first_init = False
#     def __new__(cls, *args, **kw):
#         if not cls.__instance:
#             # 把实例化出的对象给到保护变量instance
#             cls.__instance = object.__new__(cls, *args, **kw)
#         return cls.__instance
#
#     def __init__(self):
#         self.name = None
#         if not self.__first_init:
#             self.name = None
#             Singleton.__first_init = True
#     def setName(self,name):
#         self.name = name
#     def getName(self):
#         return self.name
# a = Singleton()
# b = Singleton()
# a == b
# a.setName('y')
# print(b.getName())
# print(id(a), id(b))
# try:
#     print('1111')
#     open('12.txt','r')  # 该路径无该文件
#     print('2222')
# except FileNotFoundError as e:
#     print('捕捉到异常了')
#     print('Error:错误的原因可能是{}'.format(e))
#
# # BaseException 所有异常的基类 可以捕捉全部异常类型
# try:
#     # print(aaa)              # 未定义aaa变量
#     # open('12.txt', 'r')  # 该路径无该文件
#     a =2
# except BaseException as e:
#     print('捕捉到异常了')
#     print('Error:错误的原因可能是{}'.format(e))
# else:
#     print('没有捕捉到异常，程序继续运行')

# import time
# try:
#     f = open('test.txt')
#     try:
#         while True:
#             content = f.readline()
#             if len(content) == 0:
#                 break
#             time.sleep(2)
#             print(content)
#     except:
#         #如果在读取文件的过程中，产生了异常，那么就会捕获到
#         #比如 按下了 ctrl+c
#         pass
#     finally:
#         f.close()
#         print('关闭文件')
# except:
#     print("没有这个文件")

# 异常的传递
# def test():
#     print('test1')
#     print(num)
#     print('test1结束')
# def test2():
#     print('test2')
#     try:
#         test()
#     except BaseException as e:
#         print('捕捉到了异常，异常信息时:{}'.format(e))
#     print('test2结束')
#
# test2()

# class DaxieExcept(BaseException):
#     def __init__(self,value):
#         self.value = value
#
# def main():
#     try:
#         s= input('请输入:')
#         if not s.islower():
#             raise DaxieExcept(s)
#
#     except DaxieExcept as e:
#         print('DaxieExcept:s输入的{}不是小写'.format(e.value))
# # main()
#
# def sub(a,b):
#     try:
#         return a/b
#     except BaseException as e:
#         # 这里先捕获异常用日志记录下来，再抛出异常，程序终止。如果不用抛出异常，除数为0程序也不会终止
#         print('错误信息',e)
#         raise BaseException("除数不能为0")
# sub(26,0)
import test as test
A = test.Spider()
A.loadPage(1)

