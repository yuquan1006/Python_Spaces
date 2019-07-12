#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 15:28
# @Author  : Yuquan
# @Site    : 
# @File    : 获取执行cmd的结果.py
# @Software: PyCharm

# 直接运行cmdz指令 os.system是简单粗暴的执行cmd指令，如果想获取在cmd输出的内容，是没办法获到的
import os

cmd0 = r"dir"
cmd1 = r"python C:\Users\A\Desktop\hellp.py"
# os.system(cmd1)



#获取在cmd输出的内容 os.popen popen返回的是一个file对象，跟open打开文件一样操作了
f = os.popen(cmd1, "r")
d = f.read()
print(d)
print(type(d))
f.close()

# 场景 ： 在app自动化的时候，经常用到指令：adb devices来判断是否连上了手机,那么问题来了，如何用python代码判断是否正常连上手机？

# popen返回文件对象，跟open操作一样
f = os.popen(r"adb devices", "r" )
shuchu = f.read()
f.close()

print(shuchu)  # cmd输出结果

# 输出结果字符串处理
s = shuchu.split("\n")   # 切割换行
new = [x for x in s if x != '']  # 去掉空''
print(new)


# 可能有多个手机设备
devices = []  # 获取设备名称
for i in new:
    dev = i.split('\tdevice')
    if len(dev)>=2:
        devices.append(dev[0])

if not devices:
    print("手机没连上")
else:
    print("当前手机设备:%s"%str(devices))