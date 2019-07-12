#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/7 15:48
# @Author  : Aries
# @build   : Python2.8
# @File    : 高阶函数01.py
# @Software: PyCharm

# 高阶函数:既然变量可以指向函数(函数名)，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

def add(x,y):
    f=abs  # 变量指向函数
    return f(x)+f(y)
print(add(-10,1))

def add_01(x,y,f):
    '''就是让函数的参数能够接收别的函数'''
    return f(x)+f(y)
print(add_01(10,-5,abs))

#python 内置高阶函数 map，reduce
# map()函数接收两个参数，一个是函数(函数只有一个参数)，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x**2

lists=[11,52,66,11]
lists=list(map(f,lists))
print(lists)

# list所有数字转为字符串
lists = [1,2.3,5,4,8]
lists = list(map(str,lists))
print(''.join(lists))


# reduce()函数把结果继续和序列的下一个元素做累积计算，
def adds(a,b):
    return a+b
str_a=[1,2,3,4]    #adds(1,2)作为adds的a参数，3作为b参数，他们结果继续作为a参数，和下一元素作b参数运算
# print reduce(adds,str_a)

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def ass():
    str_user = raw_input('请输入本名姓名:')
    str_users = raw_input('请输入父亲姓名:')
    lists =[]
    lists.append(str_user)
    lists.append(str_users)
    return lists

def fs(word):
    s=word[0:1].upper()+word[1::].lower()
    return s
# print map(fs,ass())

# 请编写一个prods()函数，可以接受一个list并利用reduce()求积
def prod(x,y):
    return x*y
def prods(f,lists):
    return reduce(f,lists)

# print prods(prod,[1,2,3,4])


# 把字符串'123.456'转换成浮点数123.456：
def str_float(value):
    lists=[]
    lists.append(value)
    result = map(float,lists)
    # new = reduce(lambda x:x+0,result)
    return new

# print str_float('123.456')



# filter()接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定
# 保留还是丢弃该元素。

def old(n):
    return n%2==1
# print old(2)
# print old(15)
# print list(filter(old,[1,5,8,10]))


# sorted（）它还可以接收一个比较函数（cmp=）来实现自定义的排序。
lists=[-1,-2,5,85,44]

def cmps(x,y):
    '''根据x，y比较结果直接排序'''
    if x>y :
        return 1
    if x<y:
        return -1
    return 0
new = sorted(lists,cmp=cmps)
# print new
# 也可以接受一个key=，安装该函数规则排序
new = sorted(lists,key=abs,reverse=False)
# print new


# 返回函数
# 把函数当作结果值返回
# 1.可变参数的求和
def calc_sums(*ags):
    temp=0
    for i in ags:
        temp = temp+i
    return temp
# print calc_sums(10,22,55)
#2.可变参数求和，并不直接返回结果。我想用的时候才返回
def calc_sums_01(*ags):
    def sum():
        temp = 0
        for i in ags:
            temp=temp+i
        return temp
    return sum

f = calc_sums_01(1,1555,1)  #当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
# print f()                   # 调用f（）函数是才返回求和结果
# 在函数calc_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当外部
# z函数返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。


# 匿名函数 关键字 lambda。 lambda x :x+1   冒号前面的是函数的参数，后面的返回值表达式的结果
# print map(lambda x:x*2,[1,2,3,4,5,6])               #结果 [2, 4, 6, 8, 10, 12]
# lambda x:x*2 等价于
# def fx(x):
#     return x*2


# 装饰器
def log(func):
    def wrapper(x):
        # print 'begin %s call'%func.__name__
        a = func(x)
        # print 'end %s call'%func.__name__
        return a
    return wrapper
@log
def max(x):
    temp =0
    for i in x:
        if i>temp:
            temp=i

    return temp

# print max((85,56,22,99))


# 创建偏函数。
# functolls.partial 的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
import functools
sorted_len = functools.partial(sorted,key=len)
# print sorted_len(['1','55','23323'],reverse=True)

