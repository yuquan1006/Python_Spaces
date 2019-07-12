#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6

import unittest

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 15:09
# @Author  : Yuquan
# @Site    :
# @File    : demo.py
# @Software: PyCharm
'''
unittest 只有三种结果
1.出现E 表示自己写的代码语法错误
2.出现F 测试用例不通过
3.出现. 测试通过

'''
import unittest

class TestAddFunc(unittest.TestCase):  # 测试类 继承unittest.TestCase  测试类就是多个用例的一个集合，相当于是测试用例的一个模块
    @classmethod
    def setUpClass(cls):                # 测试类前置处理
        print("测试类初始化一次--> setupclass")
    @classmethod
    def tearDownClass(cls):              # 测试类后置处理
        print("测试类后置处理--> teardownclass")

    def setUp(self):                    # 用例前置处理 比如 需要登录
        print("每个用例都初始化--> setup")
    def tearDown(self):                 # 用例后置处理 清理数据比如 退出上一个用例登录的状态
        print("每个用例都退出--> teardown")

    def testAdd01(self):                # 测试类下一个函数就是一个测试用例 测试用例的名称要以 test 开头
        result = 10-5
        hope = 5
        self.assertEqual(result, hope)     # 断言（检查点）

    def testAdd02(self):
        result = 10-12
        hope = -2
        self.assertEqual(result, hope)

if __name__ == '__main__':
    unittest.main()
