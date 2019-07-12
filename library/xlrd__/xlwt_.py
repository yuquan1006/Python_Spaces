#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/10 9:29
# @Author  : Yuquan
# @Site    : 
# @File    : xlwt_.py
# @Software: PyCharm
import xlwt

# 创建一个excel对象
work = xlwt.Workbook(encoding='utf-8')

# 创建表
worksheet = work.add_sheet('ee')

# 对单元格写入数据
worksheet.write(1, 1, '123456')
worksheet.write(0, 0, '12345')

# 保存  tip:xlrd模块0.8版本后不支持以xlsx为后缀名文件
work.save(r'C:\Users\A\Desktop\t3.xls')
# with open(r'C:\Users\A\Desktop\t2.xls', 'wb') as f:
#     work.save(f)



# 如果要对一个已存在的文件修改怎么处理？
#   1.首先先xlrd读取文件，再xlutils.copy 复制excel对象，通过get_sheet()获取的sheet有write()方法.再保存复制修改过的excel
from xlutils.copy import copy
import xlrd

work = xlrd.open_workbook(filename=r'C:\Users\A\Desktop\t.xls')
cp_work = copy(work)
sheet = cp_work.get_sheet(0)
sheet.write(1, 1, 4)
sheet.write(1, 3, 'test')
cp_work.save(r"C:\Users\A\Desktop\t.xls")


