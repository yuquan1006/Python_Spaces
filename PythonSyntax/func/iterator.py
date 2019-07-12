#!/usr/bin/env python
# encoding: utf-8
# author: 余泉
# version: python3.6
# file: iterator.py
# time: 2018\4\23 0023 16:34
from collections import Iterable
from collections import Iterator
# 迭代器  可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# for循环本质:
# for 循环在处理这些数据前，会调用 __iter__() 方法，将这些数据转化为一个迭代器，然后调用迭代器的 __next__() 方法，
# 并捕获StopIteration异常，也就实现了遍历完所有数据就会结束，并不会抛出这个异常
# 可迭代对象  可以使用isinstance()判断一个对象是否是Iterable对象(可迭代的）：
# print(isinstance([],Iterable));print(isinstance({},Iterable));print(isinstance((x for x in range(10)),Iterable))
# print(isinstance(123,Iterable))

# 迭代器：Iterator
# 判断变量是否是可以迭代
print(isinstance(range(1,10),Iterable))
print(isinstance(range(1,10),Iterator))
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance((x for x in range(10)),Iterator))
print(isinstance(123,Iterator))
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
list = [1,2,3,4]
list1 = iter(list)        #  把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(list1,Iterator))

for x in range(0,3):
    print(x)
# 等价于下面
# list2 = [0,1,2]
# lsit3 = iter(list2)
# while True:
#      try:
#         it = next(lsit3)
#         print(it)
#      except StopIteration:
#          break
# 小结 1.凡是可作用于for循环的对象都是Iterable（可迭代对象）类型
#        2.凡是可作用于next()函数的对象都是Iterator（迭代器）类型，它们表示一个惰性计算的序列
#        3.集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。


# 生成器
# def flatten(nested):
#     for sublist in nested:
#         for element in sublist:
#             yield element           # yield 的作用就是把一个函数变成一个 generator(生成器），会返回一个iterable的对象
#
# nested = [[1,2],[3,4],[5]]
# for num in flatten(nested):
#     print(num)

# 生成器方法
def repeater(value):
    while True:
        new =(yield value)
        if new is not None:
            value = new

# for x in r:
#     print(x)
# r = repeater()
# r.send("fjkfkfk")
# print(r.next())


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if L!=[]:
        (min, max) = (L[0], L[0])
        for x in L:
            if max<x:
                max = x
            if min>x:
                max = x
        print((min,max))
        return (min,max)
    else:
        return (None,None)

print(findMinAndMax([1,88,5,66]))