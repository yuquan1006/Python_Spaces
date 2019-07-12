#!/usr/bin/env python
# encoding: utf-8
# author: 余泉
# version: python3.6
# file: file_RW.py
# time: 2018\4\25 0025 17:01
# 文件读写

#               读
path = r'C:\Users\A\Desktop\1.txt'
# file = open(path,'w')
# file.write('hello')
# file.write('你好')
# file.close()
# file = open(path,'r')
# print(file.read())
# file.close()
#   read 指定参数
# file = open(path,'r')
# print(file.read(4))         # 读取前四个字符
# print(file.read(7))         # 接着四个之后读取7个
# file.close()
# #   readline
# file = open(path,'r')
# for x in  range(0,3):
#     print(str(x)+':'+file.readline())        # 读取一行,每次使用它会从已读取的下一行开始。
# file.close()
# # readlines
# import pprint
# file = open(path,'r')
# pprint.pprint(file.readlines())         # readlines返回包含文件所有内容的字符串列表, 每个元素是一行的字符串。pprint 模块的pprint方法将内容分成每个小项单行显示
# file.close
# #                   写
# path = r'C:\Users\Administrator\Desktop\2.txt'
# f = open(path,'w')
# f.write('hello\npython\n3')
# f.close()
#
# f =open(path,'r')
# lines = f.readlines()
# lines[0] = '这是用列表写入的\n2\n3'
# f.close()
# f =open(path,'w')
# f.writelines(lines)
# f.close()

#               对文件内容进行迭代
# 1.接字节处理
# f = open(path,'r')
# while True:
#     char = f.read(1)
#     if not char:
#         break
#     print(char)
# f.close()
# 2.读取所有内容
# 用read读取每一个字符
# f = open(path,'r')
# for char in f.read():
#     print(char)
# f.close()
# # 用readlines 读取每一行
# f = open(path,'r')
# for line in f.readlines():
#     print(line)
# f.close()
# # 文件迭代器                              文件对象是可以迭代的，这就意味着可以直接在for循环中对他们进行迭代
# print('----------')
# f = open(path,'r')
# for char in  f:
#     print(char)
# f.close()


#  列子
f = open(path,'w')
f.write('first line\n')
f.write('sencond line\n')
f.write('throes line\n')
f.close()
lines = list(open(path))  #
print(lines)
f.close()
first,second,third = open(path)
print(first)

# 使用序列来对一个打开的文件进行解包操作，把每行都放入一个单独的变理中，这么做是很有实用性的，因为一般不知道文件中有多少行，但它演示的文件的“迭代性”。
# 在写文件后一定要关闭文件，这样才能确保数据被更新到硬盘。
