#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 14:05
# @Author  : Yuquan
# @Site    : 
# @File    : demo7.py
# @Software: PyCharm
import time
# 知识点：封装判断方法-（断言） JS

# 1 判断元素是否存在：（由于定位不到会抛异常，所以根据是否用异常来判断）不抛异常，返回True 抛异常，返回Fasle


# # JS 定位元素
from selenium import webdriver
driver = webdriver.Chrome()
# driver.get("http://127.0.0.1:81/zentao/user-login.html")
#
# # 1.通过元素id
# js = "document.getElementById(\"account\").value=\"yuquan\";"
# driver.execute_script(js)
#
# # 2.通过name获取 注意：除了id之外其他都是复数定位，可以通过下标获取
# js = "document.getElementsByName(\"keepLogin[]\")[0].click();"
# driver.execute_script(js)
#
# # 通过标签名选取元素
# js = "document.getElementsByTagName(\"input\")[1].value='123456';"
# driver.execute_script(js)
#
# # 通过CLASS类选取元素
# js = "document.getElementsByClassName(\"form-control\")[0].value='admin';"
# driver.execute_script(js)
#
# # 通过CSS选择器选取元素
# js = "document.querySelectorAll(\"#submit\")[0].click();"
# driver.execute_script(js)
# time.sleep(2)
#
#
# # JS 处理iframe
# # 打开bug编辑页面
# driver.get("http://127.0.0.1:81/zentao/bug-create-1-0-moduleID=0.html")
# time.sleep(3)
# # 1.富文本iframe处理
# js = 'document.getElementsByClassName("ke-edit-iframe")[0].contentWindow.document.body.innerHTML="56956556";'
# driver.execute_script(js)
# # 2 普通iframe处理
# js = "document.getElementById('iframe的ID').contentWindow.document.getElementById('元素的ID')"
# driver.execute_script(js)
#


# JS 修改元素属性
driver.get("https://www.12306.cn/index/")
js = 'document.getElementById("train_date").removeAttribute("readonly");'
driver.execute_script(js)
js = "document.getElementById(\"train_date\").value='2018-02-22'"
driver.execute_script(js)
# driver.find_element_by_id("train_date").clear()
# driver.find_element_by_id("train_date").send_keys("2018-12-30 ")
time.sleep(3)


# JS 处理内嵌div滚动条
