#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6

# 知识点：显示等待- 封装到base基类中

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:81/zentao/user-chandao-L3plbnRhby8=.html")
# driver.find_element_by_css_selector("#account").send_keys(user)
# driver.find_element_by_css_selector("[name='password']").send_keys(passwd)
# driver.find_element_by_css_selector("#submit").click()
element = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element(By.CSS_SELECTOR, "#account"))
element.send_keys("admin")
element = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element(By.CSS_SELECTOR, "[name='password']"))
element.send_keys("123456")
element = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element(By.CSS_SELECTOR, "#submit"))
element.click()
driver.quit()
