#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/5 17:03
# @Author  : Yuquan
# @Site    : 
# @File    : Practice02.py
# @Software: PyCharm
# 知识点：等待，浏览器配置，浏览器基本操作,元素基本操作
from selenium import webdriver
import time
# 加载配置  解决需要cooike 免登陆
# profile_dir = r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\nsm4it57.default"
# profile = webdriver.FirefoxProfile(profile_dir)
# driver = webdriver.Firefox(profile)



driver = webdriver.Firefox()
# 学习点：浏览器基本操作
# time.sleep() 1.Sleep    线程休眠,一次有效
# 隐式等待 这里用到implicitly_wait()，它的作用是全局的，也就是只用一次就可以了，只在find_element时候起作用
# 1.只在当前页面等待 2 与time。sleep结合使用，当页面跳转卡顿使用time。sleep
driver.implicitly_wait(20)
# 打开网页
# driver = webdriver.Firefox()
# driver = webdriver.Chrome()
# driver = webdriver.Ie()
# driver.get("https://www.baidu.com")
driver.get("https://www.baidu.com")
# 设置窗口大小
driver.maximize_window() # 最大化
driver.set_window_size(1920, 520)  # 自定义分辨率

# 休眠/等待
time.sleep(2)
# 页面刷新
driver.refresh()
# 页面前进，后退
driver.get("http://www.cnblogs.com/pachongshangdexuebi/category/981644.html")
time.sleep(1)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
a = driver.find_element_by_xpath("//a[@id='blog_nav_sitehome']")
print(driver.title)  # 页面标题
print(driver.name)
print(a.text)          # 获取元素文本
print(a.tag_name)       # 获取元素标签
print(a.get_attribute("href"))      # 获取元素某个属性值
print(a.is_displayed())         # 判读元素是否显示
print(a.is_enabled())       # 元素是否可用
print(a.location)           # 获取元素位置
print(a.size)               # 过去元素大小
# 截屏
# driver.get_screenshot_as_file(r"C:\Users\A\Desktop\1.png")

# 退出
# 1.close 用于关闭当前窗口
driver.close()
# 2.quit 结束进程，关闭所有窗口
driver.quit()





