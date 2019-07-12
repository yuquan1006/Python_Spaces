#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 11:12
# @Author  : Yuquan
# @Site    : 
# @File    : 列表推导式.py
# @Software: PyCharm
# 列表推导式
# 1 轻量级循环创建列表

print(list(range(1,10)))
# 1-100奇数
print([x for x in range(1, 101,2)])
print([x for x in range(1, 101) if x%2!=0])
print(list(range(101))[1::2])

list_a = [x for x in range(1, 101, 3)]
print(list_a)

# 2 循环时使用if
list_b = [x for x in range(0, 11) if x % 2 == 0]
print(list_b)

# 3 两个for循环
list_c = [(x, y) for x in range(1, 10) for y in range(10, 20)]
print(list_c)

# 练习:如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L1 = ['Hello', 'World', 18, 'Apple', None]
print('*********************')
print([x.lower() for x in  L1 if isinstance(x, str)])


# 生成一个[[1,2,3],[4,5,6]....]的列表最大值在100以内
a = [x for x in range(1, 101)]
b = [a[x:x+3] for x in range(0, 100,3)]
print(b)

# 请写出一段 Python 代码实现分组一个 list 里面的元素,比如 [1,2,3,...100]变成 [[1,2,3],[4,5,6]....]
list_e = [x for x in range(1, 101)]
def test(list_e, b):
    list_e
    list_f = [list_e[x:x+b] for x in range(0,100,b)]
    print(list_f)
test(list_e, 6)


# set 集合数据类型 无序且不重复
a = 'ffsdf s s '
set_a = set(a)
print(type(set_a))
print(set_a)

# set、list、tuple之间可以相互转换
set_b = set(list_a)
set_c = set((1,2,3,4,5))
print(set_b,set_c)
list_g = list(set_c)
list_h = tuple(set_b)
print(list_g,list_h)

# 列表去重
list_s = [1,2,1,122,33,33,122,5,777,5]
set_s = set(list_s)
new_list = list(set_s)
print(new_list)
# 去重成功但是没有了列表当初的顺序
# 解决办法
news_list = sorted(new_list,key=list_s.index)
print(news_list)

# 杨辉三角实现(每一项有前一列的当前标+上一项,巧妙用0实现最后一项)
def test():
    mylist = [1]
    templist=[]
    while True:
        yield mylist
        mylist.append(0)
        for i in range(len(mylist)):
            templist.append(mylist[i-1]+mylist[i])
        mylist = templist
        templist = []

def test1():
    mylist = [1]
    templist=[]
    while True:
        yield mylist
        mylist.append(0)
        mylist = [mylist[i-1]+mylist[i] for i in range(len(mylist))]


n = 0
for i in test1():
    print(i)
    n += 1
    if n ==10:
        break
