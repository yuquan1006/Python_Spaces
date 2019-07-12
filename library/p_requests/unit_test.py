#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py2
import unittest
# 对abs（）函数单元测试


#  设计测试用例
# 输入正数，比如1、1.2、0.99，期待返回值与输入相同；
# 熟入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；
# 输入0，期待返回0；
# 输入非数值类型，比如None、[]、{}，期待抛出TypeError。

# add('1','1')
class test(unittest.TestCase):
    def test01(self):
        self.assertEqual(1,abs(1))
        self.assertEqual(1.2,abs(1.2))
        print('pass')
    def test02(self):
        self.assertEqual(1,abs(-1))
        self.assertEqual(1.2,abs(-1.2))
        print('pass')
    def test03(self):
        self.assertEqual(0,abs(0))
        print('pass')
    def test04(self):
        self.assertEqual('TypeError: abs() takes exactly one argument (0 given)',abs())
if __name__ == '__main__':
    unittest.main()