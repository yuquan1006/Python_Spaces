#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 10:49
# @Author  : Yuquan
# @Site    : 
# @File    : test_exe.py
# @Software: PyChar

'''  学习gui-wxpython ->迷你编辑器 生成exe文件'''


import sys
import wx

app = wx.App(False)

frame = wx.Frame(None, wx.ID_ANY, "Hollo World")
frame.Show(True)
app.MainLoop()

'''
2是创造一个wx.App实例。参数是“False”的意思是不将stdout和stderr重定向到一个窗口，这个参数是“True”对这个例子没有影响。
3创建一个顶级窗口，语法为x.Frame（parent，ID，标题）。这个例子中wx.ID_ANY wxWidgets为我们挑选一个id。
4显示窗口
5主循环，处理事件
'''

# 生成exe文件
'''
步骤：
1.cmd切换到改目录下，输入命令：pyinstaller -F -w test_exe.py     -F 生成单个可执行文件 -w 去掉控制台窗口
2.执行完成后，test_ext.py文件的目录下生成了一个dist问文件夹，exe文件就在里面

注意事项:
1.如果代码需要调用图片或者资源文件的，是不会自动导入的，需要手动复制，不然运行exe报错
2.打包时备份，不然打包失败你的代码文件就没有
3.导入模块或方法尽量精简，不要时用import * 导致打包全部导入的库

'''
