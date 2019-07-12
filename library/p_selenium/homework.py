#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 13:08
# @Author  : Yuquan
# @Site    : 
# @File    : homework.py
# @Software: PyCharm
from selenium import webdriver
import time

'''
自己随便找个网站，最好是自己公司的web网页用所学的知识，登录的场景，用代码实现
'''
# driver = webdriver.Chrome()
# driver.implicitly_wait(20)

# driver.get("http://www.moiiee.com")
# time.sleep(5)
# # 点击登录按钮
# driver.find_element_by_xpath("//li[@name='chandao' and @class='header-menu-item']/sapn").click()
# time.sleep(1)
# # 输入用户名
# driver.find_element_by_css_selector("div.chandao-left-item>input[type='text']").send_keys("18973019192")
# time.sleep(1)
# # 输入密码
# driver.find_element_by_css_selector("div.chandao-left-item>input[type='password']").send_keys("yu1234")
# time.sleep(1)
# # 点击登录
# driver.find_element_by_xpath("//div[@class='confirm-chandao']").submit()
# time.sleep(3)
# driver.quit()


# 9*9
# for i in range(1, 10):
#     for j in range(1, i):
#         print("%d * %d = %d" % (j, i, i*j), end=' ')
#     print('')

# '''
# 1、如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。  
# 例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
# 那么问题来了，求1000以内的水仙花数（3位数）
# '''
# for i in range(1, 1001):
#     g = i % 10
#     s = i // 10 % 10
#     b = i // 100
#     if g**3 + s**3 + b**3 == i:
#         print(i)
#
#
# '''
# python作业1-（截图提交）
# 问题1.如何求出列表a中，哪个数字出现的次数最多，并打印出次数
# 问题2.对列表a 中的数字从小到大排序
# 问题3.排序后去除重复的数字
# a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
# '''
# a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
# # 1
# dic = {}
# for i in a:
#     str_a = [str(i) for i in a]
#     str_as = "".join(str_a)
#     dic[i] = str_as.count(str(i))
# for i, j in dic.items():
#     print('数字{}，出现{}次'.format(i,j))
# # 2
# aa = sorted(a, key= lambda x :x ,reverse=False)
# print(aa)
# # 3
# # aaa = set(aa)
# # aaaa = list(aaa)
# # print(aaaa)
# temp = []
# for i in aa:
#     if i not in temp:
#         temp.append(i)
# print(temp)

'''
1.如果一个元素的id的动态的，该怎么定位呢？
 答：通过其他属性或层级定位+标签
2.如何知道一个元素在不在iframe上
    1.firepath工具点击该元素，看左上角显示top windows表示主界面 iframe*的情况是在iframe中
    2.通过看html，一层一一层向上是否是iframe标签
3.切换iframe时候，如何定位到iframe上，老师教了几种方法，请详细说明
    1.通过ifame便签的id/name。driver.switch_to.frame(id/name)
    2.通过定位iframe元素， a = driver.find_element_by_tag_name('iframe')  driver.switch_to.frame(a)
    3.通过iframe的索引。driver.switch_to.frame(1)    从1开始取
4.如何自动化一个弹出框是不是alert？如果不是alert该怎么去定位弹窗上的元素
    1.用firebug 去点击弹框，能点到的不是alert。如果窗口类型的切换handler操作，如果是div类型的就定位元素。
5.如果一个下拉选择框不是select的标签时候，怎么去点击下拉框的选项里面元素
    1.先点击选项框，再点击想要的选项
6.如果是select标签的下拉框，教了几种定位方法
    1.xpath直接定位（不好用） 2.Select类专业处理（index，value，text） 3.先点击选项框，再点击想要的选项
'''

'''
冒泡排序
'''
# a = [234,34443,23,2234,3334,221]
# for i in range(len(a)-1):
#     for j in range(len(a)-1-i):
#         if a[j] > a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
# print(a)


# 网易163登录
driver = webdriver.Chrome()
# driver.get("https://mail.163.com/")
# time.sleep(2)
# driver.implicitly_wait(20)
#
# iframe = driver.find_elements_by_tag_name("iframe")[0]   # 问题思路 该iframe是动态id，根据页面上的iframe标签的定位去下标
# driver.switch_to.frame(iframe)
# time.sleep(2)
# driver.find_element_by_name("email").send_keys("yuquangetpost")
# driver.find_element_by_css_selector("input[name='password']").send_keys("714729yu")
# driver.find_element_by_css_selector("a#dologin").click()
#
#
# time.sleep(2)
# driver.quit()

'''
1.写出至少10种xpath语法
2.学会在浏览器调试定位，确定是否定位到
driver.find_element_by_xpath("//*[@id='']")
driver.find_element_by_xpath("//*[@class='' and sdf='']")
driver.find_element_by_xpath("//input[@class='' ]")
driver.find_element_by_xpath("//div[@id='']//a")
driver.find_element_by_xpath("//div[@id='']/a[0]")
driver.find_element_by_xpath("//div[@id='']/../a")
driver.find_element_by_xpath("//div[contains(text(),'')")
driver.find_element_by_xpath("//div[contains(@id,'')")
driver.find_element_by_xpath("//div[text()='')")
# 浏览器调试
# 1.firepath：//*[@id="xx"]
# 2.console:$x("//*[@id=\"xx\"]")
'''


'''
1.写出至少5种css语法
2.学会在浏览器使用jquert调试定位

'''
driver.find_element_by_css_selector("#kw")
driver.find_element_by_css_selector(".kw")
driver.find_element_by_css_selector("a#kw>input")
driver.find_element_by_css_selector("a#kw[name='']")
driver.find_element_by_css_selector("input#kw[name='']/a:nth-child(1)")
浏览器调试：
console:$("a#ddd")

