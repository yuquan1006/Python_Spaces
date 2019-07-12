#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 19:00
# @Author  : Yuquan
# @Site    : 
# @File    : Func.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
# 知识点：键盘，鼠标，多窗口，iframe

driver = webdriver.Firefox()

# driver.get("https://mail.163.com/")

# 关闭百度预测功能
# driver.find_element_by_xpath("//div[@id='u1']//a[.='设置']").click()
# driver.find_element_by_link_text("关闭预测").click()


# 简单操作
# 1 输入文本
# driver.find_element_by_xpath(".//*[@id='kw']").send_keys(u"中国") # send_keys()如果是发送中文的，前面需加u，需要转码为 Unicode 国际编码
# 2.点击
# driver.find_element_by_xpath(".//*[@id='u1']/a[1]").click()
# 3.清空输入框（字符串）
# driver.find_element_by_xpath(".//*[@id='kw']").clear()
#3.submit（一般用于模拟回车键）
# driver.find_element_by_xpath(".//*[@id='su']").submit()


# 键盘事件
# 1.模拟enter建
# driver.find_element_by_xpath(".//*[@id='su']").send_keys(Keys.ENTER)
# 2.模拟F1-F12
# driver.find_element_by_xpath(".//*[@id='kw']").send_keys(Keys.F5)
# 模拟复制
# driver.find_element_by_xpath(".//*[@id='kw']").send_keys(Keys.CONTROL, 'c')
# 模拟粘贴
# driver.find_element_by_xpath(".//*[@id='kw']").send_keys(Keys.CONTROL, 'v')
# 全选
# driver.find_element_by_xpath(".//*[@id='kw']").send_keys(Keys.CONTROL, 'a')
# 剪切
# driver.find_element_by_xpath(".//*[@id='kw']").send_keys(Keys.CONTROL, 'x')
# 制表符TAB
# driver.find_element_by_xpath(".//*[@id='kw']").send_keys(Keys.TAB)


# 鼠标事件
# 1.鼠标悬停
# mouse = driver.find_element_by_xpath(".//*[@id='u1']/a[8]")
# ActionChains(driver).move_to_element(mouse).perform()    # perform 表示执行所有 ActionChains 中的行为
# 右击
# mouse = driver.find_element_by_xpath("")
# ActionChains(driver).context_click(mouse).perform()
# 双击
# mouse = driver.find_element_by_xpath(".//*[@id='u1']/a[2]")
# ActionChains(driver).double_click(mouse).perform()
# 拖放
# start_element = driver.find_element_by_link_text("xx")
# targey_element = driver.find_element_by_id("xx")
# ActionChains(driver).drag_and_drop(start_element, targey_element)


# 多窗口和句柄切换
# driver = webdriver.Chrome()
# driver.get("http://bj.ganji.com")
# h = driver.current_window_handle    # 获取当前窗口句柄
# print(h)
# driver.find_element_by_css_selector(".tabIcon.tabIcon-2").click()
# hs = driver.window_handles          # 获取所以窗口句柄
# print(hs)
# # 切换句柄
# driver.switch_to_window(hs[1])
# 1.for 循环切换
# for i in hs:
#     if i != h:
#         driver.switch_to_window(i)
#         print(i)
#         print(driver.title)

# 2.直接list第二个切换
# driver.switch_to_window(hs[0])
# print(driver.title)
# driver.close()  # 关闭新窗口
# time.sleep(2)
# driver.switch_to_window(h)  # 切换到主页


# 定位一组元素
# import random
# driver.find_element_by_css_selector("#kw").send_keys(u'余泉')
# driver.find_element_by_css_selector("#su").click()
# s = driver.find_elements_by_xpath("//div[@class='content_left']/div[@class='c-container']/h3[@class='t']/a[@target='_blank']")
# s = driver.find_elements_by_css_selector("h3.t>a")
# print(s)
# for i in s:
#     print(i.get_attribute("href"))
# t = random.randint(0,len(s))
# 直接点击该元素
# s[t].click()
# 第二种 get请求该网址
# url = s[t].get_attribute("href")
# driver.get(s[t])



# iframe 切换:
'''
frame 是整个页面的框架，iframe 是内嵌的网页元素，也可以说是内嵌的框架
'''
# 确认元素是否在ifrema中？  1.firbug中选择元素，看左上角显示：（top windows 在主界面上） （ifreame#xx* ifre框架有id/name
# 的值 ） （ifrema 无id/name  可以通过tag——name定位）  （无显示 多层ifrma层。如果第一次没有id/name的值 可以复数获取tag_name取[0]）

'''
ifrema 定位方式：1.id 2.name 3.element对象
1.如果有id/name，直接通过过id值 d.switch_to_frame(id/name的值)
2.如果没有id/name的话，通过元素定位 d.switch_to_frame(d.find_tar_name(ifrema))
3.通过页面上iframe的索引定位 d.switch_to_frame(0)
'''
# driver.get("https://mail.163.com/")
# driver.implicitly_wait(30)
# # 切换iframe
# # driver.switch_to_frame("x-URS-iframe1541819396144.811")
# # driver.switch_to.frame("x-URS-iframe")
#
# time.sleep(1)
# driver.find_element_by_name("email").send_keys('yuquangetpost')
# 跳出ifema的问题

# 从iframe中跳出主界面
# driver.switch_to.default_content()
# 多个iframa存在处理：先切换处理，在返回主界面，在进入其他iframa
# 嵌套iframa处理：
# driver.switch_to.parent_frame() # 返回上一级


# select 下拉框

driver.get("https://www.baidu.com")
# 打开搜索设置
driver.find_element_by_xpath("//div[@id='u1']//a[.='设置']").click()
driver.find_element_by_link_text("搜索设置").click()

# 1.xpath定位处理 不推荐使用 因为存在元素不可见的情况
# driver.find_element_by_xpath(".//*[@id='nr']/option[3]").click()

# select便签的专业处理
# select_element = driver.find_element_by_id("nr")
# Select(select_element).select_by_index(2)  # 下标从0开始
# Select(select_element).select_by_value(50)
# Select(select_element).select_by_visible_text("每页显示50条")


# driver.quit()

# 3 非select选项框处理
# 1.先点击选项框，再点击下一个
# driver.find_element_by_id("nr")
# driver.find_element_by_xpath(".//*[@id='nr']/option[3]").click()
time.sleep(2)



# 点击保存设置  selenium 点击不是万能的，有些元素确实点击不到
# driver.find_element_by_xpath(".//*[@id='gxszButton']/a[1]").click()  # 点击不到
# 用js处理：
js ='document.getElementsByClassName("prefpanelgo")[0].click()'
driver.execute_script(js)

# alert弹窗处理：alert confirm prompt
'''
但并不是说所有的弹框是alert，有的就是普通的一层div,直接定位就行了,有的是一个窗口，切换handler就行
'''
# alert
a = driver.switch_to.alert # 获取alert弹窗对象
t = a.text
a.accept()  # 确认

# confirm
# driver.find_element_by_xpath("xx").click() # 触发弹框
# a = driver.switch_to.alert # 获取alert弹窗对象
# t = a.text
# a.accept()  # 确认
# a.dismiss()  # 茶雕
#
# #
# a = driver.switch_to.alert # 获取alert弹窗对象
# a.sendkeys('123')
# a.accept()  # 确认
# a.dismiss()  # 茶雕
#
# # 出现横线情况： 过时语法，可以switch_to类里面提供的方法。driver.switch_to(类).再去选择
# driver.switch_to.window()
# driver.switch_to_window()