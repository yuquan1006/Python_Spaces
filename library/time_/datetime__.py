#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 10:17
# @Author  : Yuquan
# @Site    : 
# @File    : datetime__.py
# @Software: PyCharm
'''本文学习 datetime模块（date，time，datetime，timedelta）中datetime类（包含date和time）'''
from datetime import datetime
import time

# 当前的本地日期时间
now_time = datetime.today() # 2019-02-27 10:19:39.183410
now_time2 = datetime.now() # 2019-02-27 10:19:39.183410
now_time3 = datetime.utcnow() # 返回当前的UTC日期和时间019-02-27 02:32:48.213503

print(now_time, now_time2, now_time3)

# 新建datetime对象(年月日必填参数),该对象有（year，month， day，hour，minute，second，microsecond）属性
d = datetime(2019, 12, 31)
print(d.year)
print(d.day)
print(d) #  2019-12-31 00:00:00
d = datetime(2015, 6, 20, 15, 25, 6, 123456)
print(d) # 2015-06-20 15:25:06.123456

# replace 返回一个替换后的date对象
print("+++++++")
d.replace(year=2015, day=11, second=16)
print(d)

# 格式化需要的时间
d = datetime(2015, 6, 20, 15, 25, 6, 123456)
d = d.strftime("%Y_%m_%d %H:%M:%S")
print(d)

# 转换时间元祖（结构体）
d = datetime(2015, 6, 20, 15, 25, 6, 123456)
d = d.timetuple()
print(d)
ts = time.mktime(d) # mktime 将时间元祖->时间戳
print(ts)

# 将时间戳转化为datetime对象
ts = time.time()
ds = datetime.fromtimestamp(ts)
print(type(ds))
print(ds.day)


def test():
    '''计算年龄'''
    flage = False
    while not flage:
        user_inputname = input("你的姓名:")
        user_inputbirth = input("你的出生日期(如2018-2-10):")
        name, a = check(user_inputname)
        age, b = checks(user_inputbirth)
        if a and b:
            flage = True
    print('{name} 你好！\n你的年龄是:{age}'.format(name=name, age=age))
def check(user_inputname):
    try:
        '''检验输人是否合法'''
        if 0 < len(user_inputname) < 50 and user_inputname.isalpha():
            return user_inputname,True
        else:
            return None,False
    except:
        print('姓名输入错误，请重新输入')
        return None, False


def checks(user_inputbir):
    try:
        times = user_inputbir.split('-')
        year = int(times[0])
        month = int(times[1])
        day = int(times[2])
        if 8<= len(user_inputbir) <= 10 and 0 < year <= datetime.today().year and 0< month <= 12 and 0< day<=31:
            result = datetime.today().year - int(year)
            return result,True
        else:
            print('出生日期输入错误，请重新输入')
            return None,False
    except:
        print('出生日期输入错误，请重新输入')
        return None, False


test()