#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 17:46
# @Author  : Yuquan
# @Site    : 
# @File    : time_.py
# @Software: PyCharm
# 知识电：时间和日期   时间戳  时间元组 可视化时间
import time

# 当前时间戳
print("当前时间戳为：%s" % time.time())  # 1544608048.4600503
print(int(time.time()))  # 1544608048.4600503


# 时间戳 → 时间元组（结构体）
'''接收时间戳并返回当地时间下的时间元组'''
print('++++++++++')
localTime1 = time.localtime()
localTime = time.localtime(time.time())  # 将返回浮点数的时间戳方式向时间元组转换
print(localTime)       # time.struct_time(tm_year=2018, tm_mon=12, tm_mday=12, tm_hour=17, tm_min=50, tm_sec=48, tm_wday=2, tm_yday=346, tm_isdst=0)
print(localTime1)
print(localTime1.tm_year)
print(localTime1.tm_sec)


# 时间戳 → 可视化时间
print(time.ctime(time.time()))

localTime = time.asctime(time.localtime(time.time()))
print(localTime)  # Wed Dec 12 17:53:02 2018


# 时间元组 → 时间戳  mktime()
timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(time.mktime(time.strptime(timeStr,"%Y-%m-%d %H:%M:%S"))) # 时间元祖=(time.strptime(timeStr,"%Y-%m-%d %H:%M:%S"))


# 时间元组 → 可视化时间（定制）
# time.strftime(要转换成的格式，时间元组)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))



# （7）可视化时间（定制） → 时间元祖
# time.strptime(时间字符串，时间格式)
print(time.strptime('2018-9-30 11:32:23', '%Y-%m-%d %H:%M:%S'))


b = 'admin '
a = "2018-2-23"
print(a.isdigit())
print(b.isalpha())
