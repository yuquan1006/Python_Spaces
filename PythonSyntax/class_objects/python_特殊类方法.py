#!/usr/bin/env python
# encoding: utf-8
# author: 余泉
# version: python3.6
# file: python_特殊类方法.py
# time: 2018\7\2 0002 18:26
class Fatpeople(object):
    ''' 描述类信息，这是胖子类'''  # 可用 Fatpeople.__doc__ 类的描述信息
    lei = 2500
    # 初始化方法
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    # 析构方法 当对象在内存中被释放时，自动触发执行
    def __del__(self):
        print("%s %s对象马上被干掉了..." % (self.name,self.weight))
        del self.name
        del self.weight

    # 如果一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值
    def  __str__(self):
        return '{} {}'.format(self.name,self.weight)

    # 使实例能够像函数一样被调用，同时不影响实例本身 __call__()可以用来改变实例的内部成员的值。
    def __call__(self,  name, weight):
        self.name = name
        self.weight = weight
        print('__call__ with （{}, {}）'.format(self.name, self.weight))
y = Fatpeople('yuquan',185)
print(y.__module__)  # 表示当前操作的对象在那个模块 导入的话就就出导入的文件模块
print(y.__class__)     #  表示当前操作的对象的类是什么
y('yuan',25)                         # __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()
print(y.name)

print(Fatpeople.__dict__)  # 打印类里所有属性（方法/类变量），不包括实例属性
print(y.__dict__)     #打印实例所有属性，不包括类属性
print(y)

######## 用于索引操作 如Python中，如果我们想实现创建类似于序列和映射的类，可以通过重写魔法方法__getitem__、__setitem__、__delitem__、__len__方法去模拟
class Dict_me:
    def __init__(self,key,value):
        self.dict={}
        self.dict[key] = value
        print('初始化字典')
    def __getitem__(self, key):
        return self.dict[key]
        print('获取字典的value')

    def __setitem__(self, key, value):
        self.dict[key] = value
        print('设置字典的key，value')
    def __delitem__(self, key):
        del self.dict[key]
        print('删除字典的{}'.format(key))

    def __len__(self):
        return len(self.dict)
        print('获取字典的长度')
d = Dict_me('key01','value01')
print(d.__getitem__("key01"))
d.__setitem__("key02", "value02")
print(d.__len__())

class List_me:
    def __init__(self,value):
        self.dict=[]
        self.dict.append(value)
        print('初始化列表')
    def __getitem__(self, index):
        return self.dict[index]
        print('获取列表的value')

    def __setitem__(self, index, value):
        self.dict[index] = value
        print('设置列表的key，value')

    def __delitem__(self, index):
        del self.dict[index]
        print('删除列表的{}'.format(key))

    def __len__(self):
        return len(self.dict)

l =List_me(1)
print(l.__getitem__(0))
l.__setitem__(0,100)
print(l.__getitem__(0))
print(l.__len__())

