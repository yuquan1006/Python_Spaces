#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 14:14
# @Author  : Yuquan
# @Site    : 
# @File    : test_pytest.py
# @Software: PyCharm
# 知识点：pytest单元测试框架
'''pytest介绍:比unittest框架使用起来更简洁，效率更高'''


# 单个函数测试
def func(x):
    return x+2

def test_func():
    assert func(2) == 4

def test_func01():
    assert func(0) == 0

# 多个测试时：当需要编写多个测试样例的时候，我们可以将其放到一个测试类当中，如：
class TestFunc(object):
    def setup_module(self):
        print("setupmodule")

    def test_01(self):
        assert 0 == 0

    def test_02(self):
        assert 1 == 0


# 执行测试：
'''执行测试的时候，我们只需要在测试文件test_sample所在的目录下，运行py.test即可。pytest会在当前的目录下，
寻找以test开头的文件（即测试文件），找到测试文件之后，进入到测试文件中寻找test_开头的测试函数并执行'''

# pytest执行方式
'''
1、单独执行某一个py文件里所有的用例
pytest test_mod.py
2、执行目录下所有的用例
pytest testing/
会按发现规则执行该目录下符合的用例
3、单独执行某一个用例
以函数形式的用例
pytest test_mod.py::testfunc
以类形式的用例
pytest testmod.py::testclass::test_method
'''

# 编写测试用例
'''
测试文件以test_开头（以_test结尾也可以）
测试类以Test开头，并且不能带有 __init__ 方法
测试函数以test_开头
断言使用基本的assert即可
'''

# pytest 常见参数
'''
1、-k EXPRESSION
执行某个关键字的用例
用例要匹配给出的表达式；使用python的语法，匹配的范围是文件名、类名、函数名为变量，用and来区分
2、-x, --exitfirst
当遇到错误时停止测试
6、 -v, --verbose
详细结果
7、-q, --quiet
 极简结果显示
8、--junit-xml_=path
输出xml文件格式，在与jenkins做集成时使用
9、 --result-log=path
将最后的结果保存到本地文件中
'''


