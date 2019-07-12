#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 17:46
# @Author  : Yuquan
# @Site    : 
# @File    : MOCK.py
# @Software: PyCharm
from PY.library.MOCK_ import MOCK01
import unittest
from unittest import mock
class Test(unittest.TestCase):
    def test(self):
        '''支付成功场景'''
        # mock模拟支付成功
        MOCK01.zhifu = mock.Mock(return_value={"result": "success", "reason": "null"})
        result = MOCK01.zhifu_status()
        print(result)
        self.assertEqual(result,"支付成功")
    def test02(self):
        '''支付失败'''
        MOCK01.zhifu = mock.Mock(return_value={"result": "fail", "reason": "余额不足"})
        result = MOCK01.zhifu_status()
        self.assertEqual(result,"支付失败")
if __name__ == '__main__':
    unittest.main()


