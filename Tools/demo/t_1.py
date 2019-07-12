#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 15:15
# @Author  : Yuquan
# @Site    : 
# @File    : t_1.py
# @Software: PyCharm

from tkinter import *
from tkinter import messagebox

import os
#  主窗口
root = Tk()
root.title("Tools !")
root.geometry("400x200")


def main():
    print(en.get())
    files = en.get()
    if os.path.exists(files):
        try:
            zhuanhua(files)
            for i, j in enumerate(os.listdir(files)):
                q = j.split('_.')[0]
                h = j.split('_.')[1]
                fileName = str(i) + '.' + h
                curFileName = os.path.join(files, j)
                newFileName = os.path.join(files, fileName)
                os.rename(curFileName, newFileName)
                print('%s  ->  %s 文件' % (curFileName, newFileName))

            print('总共%d文件更名处理完成' % len(os.listdir(files)))
            messagebox._show(title='处理成功!',message='总共%d文件更名处理完成' %len(os.listdir(files)),icon='info')
            return True
        except BaseException as e:
            print('Error！   文件更名出错啦！可能原因:%s' % e)
            messagebox._show(title='处理失败！',message='文件更名出错啦！可能原因:%s' % e,icon="error")
            return False
    else:
        print("Error! 输入文件目录不存在！")
        messagebox._show(title='处理失败！', message='输入文件路径不存在', icon="error")

def zhuanhua(files):
    try:
        for i, j in enumerate(os.listdir(files)):
            q = j.split('.')[0]
            h = j.split('.')[1]
            fileName = str(i) + '_.' + h
            curFileName = os.path.join(files, j)
            newFileName = os.path.join(files, fileName)
            os.rename(curFileName, newFileName)
    except BaseException as e:
        print('Error！   文件更名出错啦！可能原因:%s' % e)
        messagebox._show(title='处理失败！', message='文件更名出错啦！可能原因:%s' % e, icon="error")

def exit():
    sys.exit(0)



# l = Label(root,text='欢迎小羊使用！',font=("华康少女字体", 25), fg="blue").grid(row=0,column=0,columnspan=2,rowspan=2)
# l = Label(root,text='欢迎小羊，来到文件更名处理工具:\n            ',font=("黑体", 16)).grid(row=0,column=0,columnspan=2,rowspan=2)
# font=("华康少女字体", 15), fg="blue").grid(row=0, column=0, padx=15, pady=5)

l2 = Label(root,text='更名路径: ',font=("华康少女字体", 15), fg="red").grid(row=0,column=0, padx=15, pady=5)

en = Entry(root)

en.grid(row=0,column=1, padx=15, pady=5)

start = Button(root,text='开始',command=main,bd=5,fg='green').grid(row=0,column=2,padx=15, pady=5)
exit = Button(root,text='退出',command=exit,bd=5,fg='green').grid(row=0,column=3,padx=15, pady=5)


photo = PhotoImage(file=r"C:\Users\A\Desktop\s")
Lab= Label(root,text='欢迎小羊',font = ('微软雅黑',20),image= photo)
Lab.grid(row=4,column=0)




# t = Entry(root).grid()





root.mainloop()




'''问题：无法获取entty中文本内容？
    解决：应该定义和布局进行分开：
'''