#!/usr/bin/env python
# encoding: utf-8
# author: 余泉
# version: python3.6
# file: 生成器yield.py
# time: 2018\7\18 0018 15:53

# 输出一个自定义长度的列表
def create(num):
    n=0
    a=[]
    while n<num:
        a.append(n)
        n+=1
    return a
print(create(5))


class Create():
    def __init__(self,x):
        self.a = x
        self.b = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.b<self.a:
            cu = self.b
            self.b+=1
            return cu
a = Create(10)

def create2(num):
    n=0
    while n<num:
        yield n
        n+=1
    return n


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


a = fib(10)
for i in a:
    print(i)

r = [152,56,22,412,232,56,22]

# for i in range(len(r)-1):
#     for j in range(len(r)-1-i):
#         if r[j]>r[j+1]:
#             r[j],r[j+1] = r[j+1],r[j]
# print(r)

# for i in range(len(r)):
#     index = i
#     for j in range(i+1,len(r)):
#         if r[index] > r[j]:
#             r[index], r[j] = r[j], r[index]
# print(r)
def get():
    new = []
    for i in r:
        if i not in new:
            new.append(i)
    return new
print(get())

def get1():
    for i in r:
        yield i
for i in get1():
    print(i)
