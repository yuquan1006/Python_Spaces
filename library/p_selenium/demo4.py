#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
# 知识点：unittest
import unittest
from selenium import webdriver
import time

class ChanDAOLogin(unittest.TestCase):
    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
    # def tearDown(self):
    #     self.driver.quit()
    #
    # @classmethod
    # def setUpClass(cls):
    #     pass
    #
    # @classmethod
    # def tearDownClass(cls):
    #     pass

    def setUp(self):

        self.driver.get("http://127.0.0.1:81/zentao/user-chandao-L3plbnRhby8=.html")
        time.sleep(2)

    def tearDown(self):

        self.driver.delete_all_cookies()  # 清楚cookies 相当于退出登录

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_loginsuccess(self):
        '''
        测试点：使用正确的用户名和密码登录成功
        检查点：登录成功跳转后页面存在登录用户名
        '''
        self.driver.find_element_by_css_selector("#account").send_keys("admin")
        self.driver.find_element_by_css_selector("[name='password']").send_keys('123456')
        self.driver.find_element_by_css_selector("#submit").click()
        time.sleep(2)
        try:
            a = self.driver.find_element_by_css_selector("div#userMenu>a")
            res = a.text
        except:
            res = ""
            self.assertTrue(res == "admin")
            print("登录成功用例——测试通过")
    def test_loginfail(self):
        '''
        测试点：使用正确的用户名和密码登录成功
        检查点：登录失败跳转后页面存在登录用户名
        '''
        self.driver.find_element_by_css_selector("#account").send_keys("admin12222222222")
        self.driver.find_element_by_css_selector("[name='password']").send_keys('123456')
        self.driver.find_element_by_css_selector("#submit").click()
        time.sleep(2)
        try:
            a = self.driver.find_element_by_css_selector("div#userMenu>a")
            res = a.text
        except:
            res = ""
        self.assertTrue(res != "admin12222222222")
        self.is_alert_exist()
        print("登录失败用例-测试通过")

    @unittest.skip # 无条件跳过该用例
    def test_skip01(self):
        pass

    @unittest.skipIf(1 > 0, "表达式成立跳过")  # 表达式成立跳过
    def test_skip02(self):
        pass

    @unittest.skipUnless(0, "除非为真跳过")  # 除非为真跳过
    def test_skip03(self):
        pass


    def is_alert_exist(self):
        '''判断alert是不是在'''
        try:
            time.sleep(2)
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept() # 用alert 点alert
            return text
        except:
            return ""
if __name__=='__man__':
    unittest.main()

