#!/usr/bin/env python
# encoding: utf-8
# author: 余泉
# version: python3.6
# file: faceObject.py
# time: 2018\4\23 0023 14:47
# 学习：python的面向对象的概念：继承、封装、多态（虫师博客）

# 多态 ：多态意味着就算不知道变量所引用的对象类是什么，还是能对它进行操作，而它也会根据对象（或类）类型的不同而表现出不同的行为。
# 列子：编写打印对象长度消息的函数，则只需对象具有长度（len函数可用）即可
def length_message(x):
    print(repr(x),'长度是：',len(x))            # Python 有办法将任意值转为字符串：将它传入repr() 或str() 函数      repr和str其实就是多态特性的代表
length_message('yuquan')
length_message([1,2,45,'yuquan'])


# 封装
class Man():
    def setName(self,name):
        self.name = name

    def getName(self):
        print(self.name)

a = Man()
a.setName('天空之城')
a.getName()


# 继承


# _metaclass_=type  为了确保类是新型类。把 _metaclass_=type 入到你的模块的最开始
_metaclass_=type
class OldType:
    pass
class NewType:
    pass

# 构造方法   构造方法与其的方法不一样，当一个对象被创建会立即调用构造方法。创建一个python的构造方法很简答 __init__
class Person:
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

    def greet(self):
        print(self.name,'，你好')

    def run(self):
        print('我是人类，我可以跑')

    def say_sex(self):
        print('我的心别是：',self.sex)
p = Person('余泉','男')
p.greet()
p.say_sex()


# 重写一般方法
class Student(Person):
    # def __init__(self,name):          # 可以继承超类的构造方法，也可以重写
    #     # self.name = name


    def greet(self):                    # 重写超类person 的__init__和greet方法
        print('学生',self.name,'你好')

s = Student('于玲','男')
s.greet()
s.run()                                 # 继承超类的run方法
s.say_sex()

# 构造方法必须调用其超类Bird的构造方法来确保进行基本的初始化
# 1. 使用super 函数
__metaclass__ = type  # 表明为新式类      super只能在新式类中使用
class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print
            'Aaaah...'
            self.hungry = False
        else:
            print
            'No, thanks!'


class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__()   # 当前类和对象可以作为super函数的参数使用
        self.sound = 'Squawk!'

    def sing(self):
        print
        self.sound


# 2.调用未绑定的超类构造方法
class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print
            'Aaaah...'
            self.hungry = False
        else:
            print
            'No, thanks!'


class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = 'Squawk!'

    def sing(self):
        print
        self.sound


# 属性        在下面的例子中，getSize和setSize方法一个名为size的假想特性的访问器方法，size是由width 和height构成的元组。
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self,size):
        self.width , self.height = size
    def getSize(self):
        return self.width , self.height

r = Rectangle()
r.width = 11
r.height = 12
print(r.getSize())
r.setSize((10,20))
print(r.getSize())

