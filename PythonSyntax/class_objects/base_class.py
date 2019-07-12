#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# @Version : 1.0  
# @Time    : 2018/4/17  
# @Author  : YUQUAN
# 学习重点 ：类
# 1.方法（功能）
# class  person:  # 定义一个类 person
#     def __init__(self, name):        # __init__ 方法会在类的对象被实例化时立即运行。这一方法可以对任何你想进行操作的目标对象进行初始化操作
#         self.name = name
#
#     def say(self):          # 类下的方法    类方法与普通函数只有一种特定的区别——前者必须有一个额外的名字(变量）（self），这个名字必须添加
#         print('my name is ',self.name)
#
#
# p = person('yuquan')          # 在 Person 类下创建新的实例p
# p.say()
# print(p)

# 2.数据
# 类变量是共享的（Shared）——它们可以被属于该类的所有实例访问 该类变量只拥有一个副本，当任何一个对象对类变量作出改变时，发生的变动将在其它所有实例中都会得到体现
# 对象变量由类的每一个独立的对象或实例所拥有，它们不会被共享，也不会以任何方式与其它不同实例中的相同名称的字段产生关联
class robot:
    count = 0                                # 一个类变量，用来计数机器人的数量
    def __init__(self,name):                 #  """初始化数据"""
        self.name=name                         # 一个对象变量
        print("(初始化 {})".format(self.name))
        robot.count += 1

    def die(self):
        print("{} 被杀死了!".format(self.name))
        self.__class__.count -= 1                            # self.__class__ 属性来引用它的类
        if robot.count == 0:
            print('{} 是最后一个了'.format(self.name))
        else:
            print("还有 {:d} robots 在工作.".format(robot.count))

    def say_hi(self):
        print('你好，我的主人叫我{}'.format(self.name))
    @classmethod      # 类方法  classmethod  修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
    def how_many(cls):
        print("我们还有{}个机器人".format(cls.count))


rb = robot('小羊')
print(rb.count)
rb.say_hi()
rb.how_many()


rb2 = robot('小二')
rb2.say_hi()
rb2.how_many()

rb3 = robot('小四')
rb3.say_hi()
rb3.how_many()


