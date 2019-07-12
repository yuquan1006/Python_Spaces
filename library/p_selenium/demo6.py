#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
from selenium import webdriver
import time
# 知识点：is_displayed  is_selected  is_enable
driver = webdriver.Chrome()
driver.switch_to.frame()
driver.switch_to.default_content()
'''
元素在页面的三种状态：1 不在dom中。也就是不存在元素 2.在dom里，隐藏元素，也不是不显示is_dispaly ---False
3.在dom里，显示元素，页面上能看到is_dispaly ---True

页面元素定位不到？
1.你的定位方法是不是写错了，先在浏览器上调试，确定定位方法
2.页面没加载完，元素此时不在当前屏幕，用WebDriverWait()多等几次

元素在当前地方不可被点击，被其它元素盖住了.怎么处理？
(1).移除遮挡，手工怎么操作的，代码就怎么操作，
(2).不在当前视窗里，如滚动条操作
(3).检查是不是定位错地方了– 弹出层盖住
(4).实在搞不定用—----js最后绝招
'''

# 1.is_displayed
# driver.get("http://www.baidu.com")
# # s = driver.find_element_by_xpath(".//*[@class='bdpfmenu']/a[text()='搜索设置']")
# # print(s.is_displayed())
# driver.find_element_by_xpath(".//*[@id='u1']/a[text()='设置']").click()
# s = driver.find_element_by_xpath(".//*[@class='bdpfmenu']/a[text()='搜索设置']")
# print(s.is_displayed())
# driver.quit()

# is_selected（注意是针对于select下拉框情况）
# driver.get("http://www.baidu.com")
# driver.find_element_by_xpath(".//*[@id='u1']/a[text()='设置']").click()
# driver.find_element_by_xpath(".//*[@class='bdpfmenu']/a[text()='搜索设置']").click()
# time.sleep(2)
# driver.find_element_by_xpath(".//*[@id='nr']")
# s = driver.find_element_by_xpath("//*[@id='nr']/option[1]")
# print(s.is_selected())
# s1 = driver.find_element_by_xpath("//*[@id='nr']/option[2]")
# print(s1.is_selected())
# driver.quit()


# is_selected（type = radio 单选）
# driver.get(r"D:\documents\My_Py\PY\Local\selenium\checkbox.html")
# s = driver.find_element_by_css_selector("#boy")
# print(s.is_selected())
# s.click()
# print(s.is_selected())

# is_selected（type = checkbox 多选）
# driver.get(r"D:\documents\My_Py\PY\Local\selenium\checkbox.html")
# s = driver.find_element_by_xpath("//input[@id='c2']")
# print(s.is_selected())
# s.click()
# print(s.is_selected())

# is_enable（判断元素可以被点击或者可以输入文本）
# driver.get(r"D:\documents\My_Py\PY\Local\selenium\checkbox.html")
# s = driver.find_element_by_xpath("//input[@id='c2']")
# print(s.is_enabled())
# if s.is_enabled():
#     s.click()
# time.sleep(3)
# driver.quit()

'''


'''

