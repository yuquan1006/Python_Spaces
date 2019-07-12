#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# @Version : 1.0  
# @Time    : 2018/4/18  
# @Author  : YUQUAN
# 学习重点 : 输入、输出
import pickle
# import io

# # 用户输入
# def daoxun(text):
#     return text[::-1]                   # [::-1] 返回倒序输出的text
#
# def is_daoxun(text):
#     return text == daoxun(text)            #  text是否和倒序的text相当  相当返回ture，反之false
# something = input("Enter text: ")
# if is_daoxun(something):
#     print("Yes, it is a palindrome（'回文')")
# else:
#     print("No, it is not a palindrome（'回文')")


#  文件
# \ 会去除当前空格
# content = '''\
# Today,I study io
# so i'm so cool
# '''
# file = open('test.txt','w')      # 打开文件以编辑  'r' 'w' 和追加模式'a'
# file.write(content)              # 向文件中编写文本
# file.close()                     # 关闭文件
#
# file = open('test.txt','r')
# while True:
#     readline = file.readline()   # readline 读取文件的每一行，每一行都是自带\n
#     if len(readline) == 0:       # 返回空字符时结束
#         break
#     print(readline,end='')
# file.close()



# 持久地存储对象(pickle)。通过它(pickle)你可以将任何纯 Python 对象存储到一个文件中，并在稍后将其取回
shoplist = ['banner','apple','beef']
shoplist2 = {'a':'12','b':'13'}
shoplist1 = 'i love you'
file = open('test.txt','wb')    #  open 以写入（write）二进制（binary）模式打开文件
pickle._dump(shoplist,file)    #  然后调用 pickle 模块的 dump 函数。这一过程被称作封装
file.close()
del  shoplist
file = open('test.txt','rb')
storelist = pickle.load(file)   # 通过 pickle 模块的 load 函数接收返回的对象。这个过程被称作拆封
print(storelist)
file.close()
#
# # unicode 当我们阅读或写入某一文件或当我们希望与互联网上的其它计算机通信时，我们需要将我们 的 Unicode 字符串转换至一个能够被发送和接收的格式，这个格式叫作“UTF-8”
# f = io.open("abc.txt", "wt", encoding="utf-8")
# f.write(u"Imagine non-English language here")
# f.close()
# text = io.open("abc.txt", encoding="utf-8").read()
# print(text)


# 异常   try..except 来处理异常状况
# try:
#     something = input('Enter text：')
#     print(something)
# except EOFError:
# 处理异常  我们将所有可能引发异常或错误的语句放在 try 代码块，except 子句可以处理某种特定的错误或异常
# try:
#     something = input('Enter text：')
# except EOFError:                   # 读取异常
#     print('意外的结束')
# except KeyboardInterrupt:           # 键盘输入中断
#     print('你取消了操作')
# else:                               #  else 子句将在没有发生异常的时候执行
#     print('你输入的是：{}'.format(something))
# 抛出异常
# 解读 ：我们创建了我们自己的异常类型。这一新的异常类型叫作 ShortInputException 。 它包含两个字段——获取给定输入文本长度的 length ，程序期望的最小长度 atleast 。
# 在 except 子句中，我们提及了错误类，将该类存储 as（为） 相应的错误名或异常名。这类似于函数调用中的形参与实参。在这个特殊的 except 子句中我们使用异常对象的length
# 与 atlease 字段来向用户打印一条合适的信息
# class ShortinputException(Exception):
#     def __init__(self,length,atleast):
#         Exception.__init__(self)
#         self.length = length
#         self.atleast = atleast
#
# try:
#     text = input('Enter something --> ')
#     if len(text) < 3:
#         raise ShortinputException(len(text), 3)   #你可以通过 raise 语句来引发一次异常，具体方法是提供错误名或异常名以及要抛出（Thrown）异常的对象。你能够引发的错误或异常
# # 必须是直接或间接从属于 Exception （异常） 类的派生类
#     print('其他进程正常进行')
# except EOFError:
#     print('读取异常')
# except ShortinputException as ex:
#     print(('ShortInputException: The input was ' +
#         '{0} long, expected at least {1}')
#         .format(ex.length, ex.atleast))
# else:
#     print('No exception was raised.')
# try ...finally   在 try 块中获取资源，然后在 finally 块中释放资源是一种常见的模式
# 我们按照通常文件读取进行操作，但是我们同时通过使用 time.sleep 函数任意在每打印一行后插入两秒休眠，使得程序运行变得缓慢（在通常情况下 Python 运行得非常快速）。当程
# 序在处在运行过过程中时，按下 ctrl + c 来中断或取消程序。你会注意到 KeyboardInterrupt 异常被抛出，尔后程序退出。不过，在程序退出之前，finally子句得到执行，文件对象总会被关闭。
# 另外要注意到我们在 print 之后使用了 sys.stout.flush() ，以便它能被立即打印到屏幕
import  sys
import time
# f = None
# try:
#     f = open('abc.txt')
# # 我们常用的文件阅读风格
#     while True:
#         line = f.readline()
#         if len(line) == 0:
#             break
#         print(line, end='')
#         sys.stdout.flush()
#         print("Press ctrl+c now")
# # 为了确保它能运行一段时间
#         time.sleep(2)
# except IOError:
#     print("Could not find file poem.txt")
# except KeyboardInterrupt:
#     print("!! You cancelled the reading from the file.")
# finally:
#     if f:
#         f.close()
#         print("(Cleaning up: Closed the file)")

# with  它会获取由 open 语句返回的对象  它总会在代码块开始之前调用 thefile.__enter__ 函数，并且总会在代码块执行完毕之后调thefile.__exit__(关闭文件） 。
# with open("abc.txt") as f:
#     for line in f:
#         print(line, end='')

