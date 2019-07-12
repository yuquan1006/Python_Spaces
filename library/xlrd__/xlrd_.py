#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 18:41
# @Author  : Yuquan
# @Site    :
# @File    : xlrd_.py
# @Software: PyCharm
'''
1.单元格的数据类型：0. empty（空的）,1 string（text）, 2 number, 3 date, 4 boolean, 5 error， 6 blank（空白表格）


'''
import xlrd,xlwt
# 1 获取excel中一个工作表
work = xlrd.open_workbook(filename=r'C:\Users\A\Desktop\t.xls')    # 获取excel文件对象
name = work.sheet_names()                                           # 获取excel中全部sheet名字（返回列表）
sheet = work.sheet_by_index(0)                                      # 获取sheet对象

#2 行的操作
# nrows = sheet.nrows         # 获取sheet中有效行数
# content = sheet.row(1)      # 获取指定行的单元格对象组成的列表
# values = sheet.row_values(5, start_colx=0, end_colx=None)   # 返回由该行中所有单元格的数据组成的列表
# type = sheet.row_types(0,start_colx=0, end_colx=None)       # 返回由该行中所有单元格的数据类型组成的列表 例[1, 0, 0, 0, 0, 0]
# length = sheet.row_len(5)   # 返回该列的有效单元格长度
#
#
# # 列的操作
# ncol = sheet.ncols           # 获取列表的有效列数
# content = sheet.col(1)       # 返回由该列中所有的单元格对象组成的列表
# value = sheet.col_values(0, start_rowx=0, end_rowx=None)  # 返回由该列中所有单元格的数据组成的列表
# type = sheet.col_types(0, start_rowx=0, end_rowx=None)    # 返回由该列中所有单元格的数据类型组成的列表 例[1, 0, 0, 0, 0, 0]
#
# # 单元格操作
# objects = sheet.cell(0, 0)   # 返回单元格的对象 例text:'a1'
# type = sheet.cell_type(0, 0) # 返回单元的数据类型（数字表示） 例 1- string（text）
value = sheet.cell_value(0, 0)  # 返回单元格的数据

print(value)