#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 11:19
# @Author  : Yuquan
# @Site    : 
# @File    : ready_tkinter.py
# @Software: PyCharm

# day01：熟悉tkinter

import tkinter

# 创建一个GUI程序： 1.导入tkinter模块，创建控件 2.指定控件的master，既这个控件属于哪一个  3.告诉GM(geometry manager)有一个控件产生了

import tkinter as tk
from tkinter import *

# 主窗口
# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__()
#         self.master = master
#
#         self.pack()

# 1.第一个文本输入框
# root = Tk()
# Entry(root,text='请输入文件目录路径：例如（C:/xx/xx）').pack()
# root.mainloop()
# #上面的代码目的是创建一个Entry对象，并在Entry上显示'input your text here',运行此代码，并没有看到文本的显示，由此可知与Lable和Button不同，Entry的text属性不可以设置Entry的文本
# 2.在Entry中设定初始值，使用textvariable将变量与Entry绑定
root =  Tk()
e = StringVar()
entry = Entry(root,textvariable=e)
e.set('请输入文件目录路径：例如（C:/xx/xx）')
entry.pack()
root.mainloop()



# if __name__ == '__main__':
    # root = tk.Tk()  # 构造窗体
    # root.title('For to xiaoyang')
    # root.geometry("980x500")  # 设置窗口大小
    # root.resizable(1000,5000)
    # app = Application(master=root)
    # tk.mainloop()



