#!/usr/bin/env python
# encoding: utf-8
# author: 余泉
# version: python3.6
# file: 面向对象.py
# time: 2018\7\9 0009 17:07

class Person:
    def __init__(self,name):
        self.__name = name

    def __say(self):
        print('{}在说话'.format(self.__name))
    def say(self):
        self.__say()

    def getName(self):
        return self.__name

    def setName(self, newname):
        if len(newname) >= 1:
            self.__name = newname

        else:
            print('error:名字长度需要大于或者等于2')

p = Person('yuquan')
# print(p.name)
p.say()
print(p.getName())
p.setName('yu')
print(p.getName())
import os
print(os.path.split(os.path.realpath(__file__))[1])
# print(os.path.dirname(os.path.realpath))
print(os.listdir(os.getcwd()))

class A:
    def __init__(self,name):
        self.name = name
    def test_A(self):
        print('---A--')

class B:
    def test_A(self):
        print('---B--')

class C(B,A):
    def __init__(self,name):
        super().__init__(name)
    def test_A(self):
        print('---C--')
    def getName(self):
        return self.name
c = C('余泉')
c.test_A()
print(c.getName())

'''ython中的运行方法。没有谁规定test方法是接收的参数是什么类型的。test方法只规定，接收一个参数，调用这个参数的prt方法。在运行的时候如果这个参数有prt方法，python就执行，
如果没有，python就报错，因为abc都有prt方法，而d没有，所以得到了上边得结果，这就是python的运行方式'''
class E:
    def prt(self):
        print('A')
class F:
    def prt(self):
        print('B')
class C:
    def prt(self):
        print('C')
class D:
    pass

def test(a):
    a.prt()

a,b,c,d = E(),F(),C(),D()
test(a)


class Stu:
    # 类属性（公共属性）
    xuefei = 13500
    __kecheng = ['yu','shu','ying']
    def __init__(self,name,age):
        # 实例属性（对象的属性）
        self.__name = name # 私有对象属性
        self.age =age

s = Stu('yu',2)
print(s.xuefei)     #正确  实例对象访问类属性
print(Stu.xuefei)   # 正确    类对象访问类属性
print(s.age)        # 正确        实例对象访问实例属性
# print(Stu.age)      # 错误     类对象无法访问实例属性
# print(s.name)       # 错误      实例对象无法访问私有的实例对象属性
# print(s.__kecheng)      # 错误    实例对象无法访问私有的类属性
# print(Stu.__kecheng)      # 错误    类对象无法访问私有的类属性
s.age=23
print(s.__dict__)


class People:
    country ='china'

    # 类方法，用classmethod来进行修饰
    @classmethod
    def getCountry(cls):
        return cls.country
    @classmethod
    def setCountry(cls,country):
        cls.country =country
    @staticmethod
    # 静态方法 不如额外的参数（cls,self）或参数的属性就可以直接用的方法适合定义成静态方法
    def getcountry():
        return People.country
print(People.getcountry())
p = People()
print(People.getCountry())  # 可以通过类对象访问
print(p.getCountry())       # 可以通过实例对象访问
p.setCountry('reben')
People.setCountry('renben')
print(People.getCountry())  # 可以通过类对象访问
print(p.getCountry())

print('111111111111111')
print(p.country)
print(People.country)
p.country = 'RIBEN'
print(p.country)
print(People.country)
print(p.__dict__)
print(People.__dict__)
print(People.getCountry())
print(p.getCountry())
