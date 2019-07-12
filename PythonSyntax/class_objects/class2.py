#!/usr/bin/python
#author         :YUQUAN
#projectName    :huice_base
#date           :
#version        :PYTHON3.6
#File           :class2.py
# 类与对象
# if __name__ == '__main__':
import my_print   # 导入my_print文件时，会导入该文件下所有东西。如果只想调用my_print()方法，就可以在my_Print文件里加入if __name__ == '__main__':
my_print.my_print()


# 类是对某一类具有共同特点的事物的抽象，是在概念上的一个定义。比如 人。动物。学生。但是单独说这三个概念的时候，不代表任何一个具体的个体
# 类的具体实例叫做【对象】 【类的实例】 【实例化一个类】  学生是一个类，张三是一个的学生他就是学生类的实例、学生对象

#
class SchoolStudebt:
    # 定义类变量
    xuefei = 12800
    SchoolStudebtname = 'NewDream'

    # 定义构造函数/初始化函数
    def __init__(self,name,age=20,score=0):  #self 表示类的当前对象
        # 定义成员变量
        self.name = name
        self.age = age
        self.score = score

    #定义成员方法
    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    #定义类方法
    @classmethod
    def get_xuefei(cls):
        return cls.xuefei
    @classmethod
    def set_xuefei(cls,xuefei):
        cls.xuefei = xuefei

    #定义静态方法
    @staticmethod
    def get_xuefei2():
        return SchoolStudebt.xuefei
    @staticmethod
    def get_scoolname():
        return SchoolStudebt.SchoolStudebtname

#定义一个类的对象/实例
yu=SchoolStudebt('yuquan',age=21,score=100)
# 修改和访问类的类变量
SchoolStudebt.xuefei=9000
print(SchoolStudebt.xuefei)
# 访问类方法
print(SchoolStudebt.get_xuefei())
print(yu.get_xuefei())
# 访问成员变量
SchoolStudebt.name='yggu'
print(SchoolStudebt.name)

