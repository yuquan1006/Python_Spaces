#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
import unittest,requests
from chandao_login import  login,is_login_success

class TestChandao_Login(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        self.s.close()

    def test_01(self):
        res = login(self.s, "admin", "e10adc3949ba59abbe56e057f20f883e")
        # 实际结果
        result = is_login_success(res)
        # 期望结果 登录成功
        self.assertTrue(result)
    def test_02(self):
        res =  login(self.s, "admin22", "e10adc3949ba59abbe56e057f20f883e")
        result = is_login_success(res)
        # 期望结果 登录成功
        self.assertFalse(result)

if __name__ == '__main__':
        unittest.main()
