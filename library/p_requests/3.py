#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
from requests_demo01.chandao_login import login,is_login_success
import unittest,requests,ddt
data =[
    {"user":"admin1","psw":"e10adc3949ba59abbe56e057f20f883e", "expect":True},
    {"user":"admin2","psw":"e10adc3949ba59abbe56e057f20f883e", "expect":True},
    {"user":"","psw":"e10adc3949ba59abbe56e057f20f883e", "expect":False},
]
# print(data)
@ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
    def tearDown(self):
        self.s.close()

    @ddt.data(*data)
    def  test_01(self, testdata):
        print("本次测试数据：%s" % testdata)
        user = testdata['user']
        psw = testdata['psw']
        expect = testdata['expect']
        res = login(self.s, user, psw)
        # 实际结果
        result = is_login_success(res)
        # True断言 实际结果 == 期望结果
        self.assertTrue(result == expect)
if __name__ == '__main__':
    unittest.main()