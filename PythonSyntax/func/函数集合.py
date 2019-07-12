#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 8:56
# @Author  : Yuquan
# @Site    : 
# @File    : temp.py
# @Software: PyCharm
import time,xlrd
# -----------------------------Python 内置函数------------------

class Demo(object):
    def t(self):
        print("这是普通类中的方法")
    @staticmethod
    def t1():
        print("这是静态方法 无需实例化类姐可以使用")
		
def allFunc(iterable):
    '''空、0、false返回false  空元组、空列表返回值为True，这里要特别注意'''
    print("可迭代参数 iterable 中的所有元素是否都为Ture? ", all(iterable))
	
def anyFunc(iterable):
    '''any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
'''
    print("可迭代参数 iterable 中的所有元素是否都为False?", any(iterable))
	
def evalFunc(x,y):
    ''' 函数用来执行一个字符串表达式，并返回表达式的值。'''
    print(eval("3*x"))
    print(eval("int(y)"))
def isinstanceFunc(a):
    '''isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。'''
    print(isinstance(a,int))

def powFunc(x,y):
    '''pow() 方法返回 （x的y次方） 的值。内置方法会把参数作为整型，而 math 模块则会把参数转换为 float。'''
    import math
    print(pow(x,y))
    print("math.pow(100, 2) : ", math.pow(x, y))

def sumFunc(iterable):
    print(sum(iterable))
    print(sum(iterable, 2)) # # iterable计算总和后再加 2

def execfileFunc():
    '''用来执行一个文件。'''
    with open(r'C:\Users\A\Desktop\1.py', 'r') as f:
        exec(f.read())



def filterFunc(func, seq):
    '''filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表
接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。'''
    print(list(filter(func ,seq)))

def is_int(value):
    if isinstance(value, int):
        return True
    else: return False

def mapFunc(func, seq):
    '''map() 会根据提供的函数对指定序列做映射。
    第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。'''
    print(list(map(func, seq)))

def sortedFunc():
    '''sorted() 函数对所有可迭代的对象进行排序操作。'''
    lists = [2,1,333,20]
    newlist = sorted(lists, reverse=False)
    print(newlist)
    m =  [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    newlist = sorted(m, key=lambda x :x[-1], reverse=True)
    print(newlist)
    dict = {'john':"1" , 'mk':"20" ,"mk":"6"}
    newlist = sorted(list(dict.items()), key=lambda x : x[-1], reverse=False)
    print(newlist)

def execlFunc(fileName = r"C:\Users\A\Desktop\bill20181208.xls"):
    work = xlrd.open_workbook(fileName)
    sheet = work.sheet_by_index(0)
    firstRow = sheet.row(0)
    print(firstRow)
    allRow = sheet.nrows
    allCol = sheet.ncols
    print(allCol)
    print(allRow)
    # 先循环全部的行数，从第二行开始
    lists = []
    for i in range(1, allRow):
        temp = {}
        # 获取每一行的值（列表）
        getRowVaule = sheet.row(i)
        # print(getRowVaule)
        # 循环每一行的全部列
        for j in range(allCol):
            temp[firstRow[j].value] =getRowVaule[j].value
            # print(temp)
        lists.append(temp)
    print(lists)

if __name__ == '__main__':
    # mapFunc(len ,["2332",[00],(1,1)])
    sortedFunc()

    # new =  filterFunc(is_int, (1,"1000",100))

    # execlFunc()
    # # test01()
    # print(type([11]))
    # print(type(iter([11])))
    # execfileFunc()
    # sumFunc([1,1,1])
    # powFunc(2,3)
    # isinstanceFunc([])
    # evalFunc("1","123")
    # Demo.t1()
    # allFunc([0,1,5])
    # anyFunc([])
    # anyFunc((0,'',False))
    # a(["中华", "美国", "俄罗斯"])
    #
    # print(int("61",base=10))
    # print(ord('0'))
    # print(chr(98))
    # print(str([1,5,9]))

    # 题目：列表转换为字典。
    s = [1,1,3,3]
    d = dict.fromkeys(s, "")
    a = ["a", "b"]
    b = [11,22]
    print(dict())
    print(d)
    import json
    str2 = 'key:{"a":1}'

    print(eval("{str2}"))
    c = json.loads(c)
    print(c)
    print(type(c))