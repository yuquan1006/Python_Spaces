#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 16:54
# @Author  : Yuquan
# @Site    : 
# @File    : 2019_02-19.py
# @Software: PyCharm

a = 123
b = 125.11
print(type(a))
print(type(b))
print(type(int(b)))

c = True
f = False
print(type(c),type(f))
print(type(bool('True')))

d = '1=24'
print(type(d),type(str(c)))
# 切片
print(d[0])
print(d[::])
print(d[::-1])
print(d[1:2])
print(d[::2])
# 方法
print(d.find("0"))  # 存在返回小标值，不存在返回-1
print(d.index("1"))  # 存在返回小标值,不存在报错
print(d.count('0'))  # 返回‘0’出现次数
print(d.replace('1','2',1))  #  替换字符串,表示把1替换成2替换1次.注意新建操作
print(d.split('='))  # 返回切割后的列表
print(d.isdigit())  # 判断是否全是数
print(d.isalpha())  # 判断是否全是字母
print(d.isalnum()) # 判断是否全是字母或数字

# t = (1,)
# l = [1,2,3]
# print(type(t),type(tuple(l)))
#
l = [1,2,3]
dicts = {"a1":1,"a2":2}
print(type(l),type(list(dicts)))
print(list(dicts))
# 小标取值
print(l[0])
l[0] = 25 # 小标改值
print(l)


# 方法
l.append('add01')  # 添加一个元素
print(l)
l.insert(0,'insert')  # 插入一个元素，可根据下标操作
print(l)
l.extend([00,55]) # extend可以将另一个集合中的元素逐一添加到列表中
print(l)

if 25 in l:     # 指定的元素是否存在
    print('yes in')
# 删除元素
del l[0]
print(l)
# del l
# print(l)
l.pop()
l.pop(0)
print(l)
# l.remove('0')
print(l)
# 排序
# l.sort()
# print(l)
# new = sorted(l,reverse=False)
# print(new)

#
dicts = {"a1":1,"a2":2}
print(type(dicts))
print(type(dicts.keys()))
print(list(dicts.keys()))
for i in dicts.keys():
    print(i)

#
#
#
# print(eval("123+2"))


# 写一个类，将一个数组中全部数字加1，并返回结果和
class Sums(object):
    def __init__(self,lists):
        self.lists = lists

    def sums(self):
        new = []
        for i in self.lists:
            i += 1
            new.append(i)
        return sum(new)


# 写一个类，随机生成10个数，并打印最小三个数
import random
class Ran(object):
    def __init__(self):
        self.ran_list=[]
        while len(self.ran_list)<10:
            self.ran_list.append(random.randint(0,100))

    def printMin(self):
        for i in range(len(self.ran_list)-1):
            for j in range(len(self.ran_list)-1-i):
                if self.ran_list[j]>self.ran_list[j+1]:
                    self.ran_list[j],self.ran_list[j+1] = self.ran_list[j+1],self.ran_list[j]

        print(self.ran_list)
        print("最小的三个数:{0} {1} {2}".format(self.ran_list[0], self.ran_list[1],self.ran_list[2]))


# 冒泡排序
def bubble_sort(L):
    for i in range(len(L)-1):
        for j in range(len(L)-1-i):
            if L[j] > L[j+1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    print("冒泡排序后结果为:{}".format(L))
    return L

# 水仙花：水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身
def find_daffodil():
    temp = []
    for i in range(100, 1000):
        baiwei = i//100
        shiwei = i//10 % 10
        gewei = i % 10
        if gewei ** 3 + baiwei ** 3 + shiwei ** 3 == i:
            temp.append(i)
    print('1000之内的水仙数有{}'.format(temp))

# 如何遍历电脑某个文件夹下所有的文件
import os
def look_allfile(rootPath):
    if not os.path.exists:
        print('路径不存在')
        return None
    for path,dirs,files in os.walk(rootPath):
        print(path,dirs,files)
        for file in files:
            print(os.path.join(path,file))


#  例如：如何判断一个文件是否存在，如果存在统计她的行数；不存在则建立这个文件并输入“hello”
import os
def operation(filePath):
    if not os.path.exists(filePath):
        with open(filePath, "wb") as f:
            f.write("hello")
    with open(filePath, 'rb') as f:
        lines_list = f.readlines()
        result = len(lines_list)
    return result

# 1
def test1():
    a = [1,0,10,3,-5,-855]
    result = [x for x in a if x>0]
    result1 = [x for x in a if x<0]
    print("该列表中存在正数{0}个，负数{1}个".format(len(result),len(result1)))


# 2 字符串切片 字符串 "axbyczdj"，如果得到结果“abcd”
def test2():
    a = "axbyczdj"
    result = [a[x] for x in range(0,len(a),2)]
    result = ''.join(result)
    print(result)
def test2_2():
    a = "axbyczdj"
    print(a[::2])

# 字符串切割 已知一个字符串为“hello_world_yoyo”, 如何得到一个队列 ["hello","world","yoyo"]

def test3():
    a = "a_b_c"
    print(a.split('_'))

# 已知一个队列,如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到：[3, 5, 1, 7]
def test4():
    a = [1,2,3,4]
    a.insert(3,a[0])
    print(a[1::])

# 已知 a = 9, b = 8,如何交换 a 和 b 的值，得到 a 的值为 8,b 的值为 9
def test5():
    a = 9
    b = 8
    a,b =8,9
    print(a,b)

# 水仙数
def test6():
    for i in range(100,1000):
        ge = i%10
        shi = i//10%10
        bai = i//100
        if ge**3 + shi**3 + bai**3 == i:
            print("水仙数有:%s"%i)

# 完全数
def test7():
    for i in range(0,1000):
        sums = []
        for k in range(1, i):
            if i%k == 0:
                sums.append(k)
        if sum(sums) == i:
            print('完全数{}'.format(i))

# 排序
def test_maopao(a=[12,3,44333,222]):
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    print(a)

def test_chose(a=[12,3,44323,22]):
    for i in range(len(a)-1):
        index = i
        for j in range(index+1,len(a)):
            if a[index]>a[j]:
                a[index],a[j] = a[j],a[index]
    print(a)

def test8():
    a = [1,22,3,433,33]
    a.sort(reverse=True)
    print(a)

def test9():
    a = {"a":1222,"b":233}
    print(sorted(a.items(),key=lambda x: x[-1]))

# 计算 n!,例如 n=3(计算 321=6)， 求 10!
def fn(n=10):
    if n == 1:
        return 1
    return fn(n-1)*n

# 已知一个数列：1、1、2、3、5、8、13、。。。。的规律为从 3 开始的每一项都等于其前两项的和，这是斐波那契数列。求满足规律的 100 以内的所以数据
def test10(n =100):
    a,b = 0,1
    s = [1]
    while b<n:
        s.append(b)
        a,b = b,a+b
    print(s)


#
import re,sys
def test11():
    while True:
        email = input("请输入：")
        if email == "Q":
            sys.exit(0)
        result = re.match(r"^[0-9 a-z A-Z]*@[0-9A-Za-z]+\.com$",email)
        if result:
            user = email[:email.find("@")]
            company = email[email.find("@")+1:email.find(".")]
            print(user,company)


        else:
            raise BaseException("incorrect email format")


def test21(email):
    a = re.match(r"^[0-9a-zA-Z]+@[0-9a-zA-Z]+\.com$",email)
    if a:
        user = re.findall(r"^(.+?)@",email)[0]
        com = re.findall(r"@(.+?)\.com",email)[0]
        print("用户:%s 公司:%s"%(user,com))
        return True
    else:
        print("incorrect email format")
        return False


def test22():
    while True:
        a = input("请输入")
        if a == "Q" or a == "q":
            exit()
        else:
            if test21(a):
                break

# 如何遍历查找出某个文件夹内所有的子文件呢？并且找出某个后缀的所有文件
def test23():
    path =r'C:\Users\A\Desktop\shell'
    rule = '.txt'
    result = []
    for path,dir,file in os.walk(path):
        for f in file:
            filename = os.path.join(path,f)
            if filename.endswith(rule):
                result.append(filename)
    for i in result:
        print(i)


if __name__ == '__main__':
    # s = Sums([1, 2])
    # print(s.sums())
    # r = Ran()
    # r.printMin()
    # bubble_sort([256,255,1316,45,115])
    # find_daffodil()
    # print(os.path.exists(r'C:\Users\A\Desktop\5'))
    # look_allfile(r'C:\Users\A\Desktop\temp\test')
    # print(operation(r'C:\Users\A\Desktop\1.html'))
    test23()
