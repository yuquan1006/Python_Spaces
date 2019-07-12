#!/usr/bin/env python
# encoding: utf-8
# author: 余泉
# version: python3.6
# file: RE模块学习.py
# time: 2018\7\2 0002 14:20
import re
# re模块的使用
# 1、使用 compile() 函数将正则表达式的字符串形式编译为一个 Pattern 对象
# 2、通过 Pattern 对象提供的一系列方法对文本进行匹配查找，获得匹配结果，一个 Match 对象。
#  3.最后使用 Match 对象提供的属性和方法获得信息，根据需要进行其他的操作




#     正则表达式语法  # http://www.liujiangblog.com/course/python/73
'''
1. 普通字符
        表达式	匹配
    普通字符 匹配自身       表达式c，在匹配字符串abcde时，匹配结果是c
2.元字符
        表达式	匹配
    .	小数点可以匹配除了换行符\n以外的任意一个字符
    |	逻辑或操作符
    []	匹配字符集中的一个字符
    [^]	对字符集求反，也就是上面的反操作。尖号必须在方括号里的最前面
    -	定义[]里的一个字符区间，例如[a-z]
    \	对紧跟其后的一个字符进行转义
    ()	对表达式进行分组，将圆括号内的内容当做一个整体，并获得匹配的值

3.转义字符
    表达式	匹配
    \r, \n	匹配回车和换行符
    \t	匹配制表符
    \\	匹配斜杠\
    \^	匹配^符号
    \$	匹配$符号
    \.	匹配小数点.
4.预定义匹配字符集
    表达式	匹配
    \d	任意一个数字，0~9 中的任意一个
    \w	任意一个字母或数字或下划线，也就是 A~Z,a~z,0~9,_ 中的任意一个
    \s	空格、制表符、换页符等空白字符的其中任意一个
    \D	\d的反集，也就是非数字的任意一个字符，等同于[^\d]
    \W	\w的反集，也就是[^\w]
    \S	\s的反集，也就是[^\s]
5.重复匹配
    表达式	匹配
    {n}	表达式重复n次，比如\d{2}相当于\d\d,ca{3}相当于aaa
    {m,n}	表达式至少重复m次，最多重复n次。比如ab{1,3}可以匹配ab或abb或abbb
    {m,}	表达式至少重复m次，比如\w\d{2,}可以匹配a12,_1111,M123等等
    ?	匹配表达式0次或者1次，相当于{0,1}，比如a[cd]?可以匹配a,ac,ad
    +	表达式至少出现1次，相当于{1,}，比如a+b可以匹配ab,aab,aaab等等
    *	表达式出现0次到任意次，相当于{0,}，比如\^*b可以匹配b,^^^b等等
6.位置匹配
    表达式	匹配
    ^	在字符串开始的地方匹配，符号本身不匹配任何字符
    $	在字符串结束的地方匹配，符号本身不匹配任何字符
    \b	匹配一个单词边界，也就是单词和空格之间的位置，符号本身不匹配任何字符
    \B	匹配非单词边界，即左右两边都是\w范围或者左右两边都不是\w范围时的字符缝隙    

7.贪婪与非贪婪模式
    在修饰匹配次数的特殊符号后再加上一个?问号，则可以使匹配次数不定的表达式尽可能少的匹配  比如 （.+） -> (.+?)
    
'''
# Email地址	 yuquangetpost@163.com
str = '1251523660@qq.com'
pattern = r"^\w{6,20}@[0-9 a-z]{2,3}\.com"
pattern = r"^\w+(\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
result = re.search(pattern,str)
print(result.group())

# 手机号码


# 正则表达式匹配规则
# 字符
# .       表示除换行符之外任意字符
# 一般字符 匹配自身
# \       转义字符，使后一个字符改变原来的意思
# [..]    字符集，可以是任意字符，也可以给出是范围 如[aldl],[a-z0-9]。如果第一个字符时^表示取反

# pattern 方法如下
    # match 方法：从起始位置开始查找，一次匹配
    # search 方法：从任何位置开始查找，一次匹配
    # findall 方法：全部匹配，返回列表
    # finditer 方法：全部匹配，返回迭代器
    # split 方法：分割字符串，返回列表
    # sub 方法：替换
# str_ = '1ol1one1ll2twothree34@four'
# pattern  = re.compile(r'[0-9]{2}@')
# 匹配成功时，返回一个 Match 对象，如果没有匹配上，则返回 None。
# content = pattern.match(str_)
# print(content)
# content = pattern.search(str_)
# print(content.group())
# pattern = re.compile(r'l.{2}')
# content = pattern.findall(str_)
# print(content)
#

#
# t = "I love study . it's good feel"
# data = '"token": "affkfkkfkfkfk", "active": "Ture"'
# # search = re.compile(r'\w*oo\w*')
# # print(re.findall(search))
#
# # mathch() 匹配string 开头
# print(re.match('I(.+)$', "I love study . it's good feel", re.S).group())
#
# # search() 在string中进行搜索 flags 参数修改正则表达式的匹配方式： re.S 使.匹配包括换行在内的所有字符  re.I使匹配对大小写不敏感
# print(re.search('(.+?)com', 'www.4comrunoob.5com',re.S).group())
# print(re.search('"token": "(.+?)"', data).group())              # 匹配的整个表达式的字符串
# print(re.search('"token": "(.+?)"', data).group(1))             # 匹配你查询的字符串
#
#
# # findall() 在string中查找所有 匹配成功的组并返回一个列表, (.+?) 非贪婪模式取一个就不找了  （.+）贪婪模式
# data = '"token": "affkfkkfkfkfk", "active": "Ture"'
#
# print(re.findall('"token": "(.+?)"', data, re.I))
# a = ''.join(re.findall('"token": "(.+?)"', data))
# print(a)
#
# #
# # [a-zA-Z0-9] 匹配大小写字母与数字
# # 　　[a-zA-Z] 匹配大小写字母
# # 　　@ a@b a@b (字符转义)
# # 　　. a.b a.b (字符转义)
# # 邮箱格式函数
# # def emails(e):
# #     if len(e) >= 5:
# #         if re.match("[a-zA-Z]+@+[a-zA-Z0-9]+.+[a-zA-Z]",e) != None:
# #             return '邮=箱=格式正确!'
# #         else:
# #             return '邮=箱=格式错误！'
# # e = input("请输入email:")
# # a = emails(e)
# # print(a)
# #
# # def emails(account):
# #     if len(account) >= 5:
# #         if re.match("[a-zA-Z0-9]+@+[a-zA-Z0-9]+.+[a-zA-Z]",account) != None:
# #             return '{}邮箱格式正确'.format(account)
# #         else:
# #             return  '{}邮箱格式错误'.format(account)
# #
# # a = input('请输入email:')
# # b = emails(a)
# # print(b)
# # 获取一个uRL的拓展名
# address= 'sadf/lsdkjflsdkj/sllls/232323.jsp'
# # def getname(url):
# #     listt = ['.php', '.html', '.asp', '.jsp']
# #     for i in listt:
# #          name = re.findall(i,url)
# #          if len(name)>0:
# #             return i
# #
# # a = getname(address)
# #
# # # 获得当前时间的前一天(或前一秒)
# # import time,datetime
# # # 当前时间
# # now_time = datetime.datetime.now()
# # print(now_time)
# # yesterday = now_time + datetime.timedelta(days = -1,hours=-5,seconds=-1)
# # print(yesterday)
# #
# # import datetime
# # # now = datetime.datetime.now()
# # # print(now)
# # # d = now+ datetime.timedelta(days= -1)
# # # print(d)
#
# title = u'你好，hello，世界'
# #
# pattern = re.compile('[\u4e00-\u9fa5]+')
# result = pattern.findall(title)
# print(result)