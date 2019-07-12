#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# @Version : 1.0  
# @Time    : 2018/4/13  
# @Author  : YUQUAN  
# @File    : dyy_test.py
# 学习重点 format-print
name='yuqunan'
count=2
# format()函数，引用变量
print('我要引用{}'.format(name))
print('{0}\n我要引用{1}个变量\n你信吗'.format(name,count))


# 使用下划线填充文本，并保持文字处于中间位置
#  使用 (^) 定义 'hello'字符串长度为9/指定字符串长度
print('{0:_^9}'.format(name))
print('{na} is {sex}'.format(na='yuquan',sex='supper man'))
# print 总是会以一个不可见的“新一行”字符（ \n ）结尾，因此重复调用 print 将会在相互独立的一行中分别打印。为防
# 止打印过程中出现这一换行符，你可以通过 end 指定其应以空白结尾
print('c',end='')
print('d',end='')
# end 指定以空格结尾
print('e',end='   ')
print('f',end='')

#转义
print('')
print('What\'s your name ?')
print("\"What's your name ?\"")
print('''"What's your name?"''')

# 逻辑行-物理行 ;分割表示语句结束
i = 5
print(i)
i = 7; print(i)








