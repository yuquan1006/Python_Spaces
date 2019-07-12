#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
import ddt
import unittest

data = [
    {"user": "111", "psw": "1111", "expect": True},
    {"user": "222", "psw": "2222", "expect": True},
    {"user": "333", "psw": "3333", "expect": False},
]

@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(*data)
    def test_login(self, abc):
        print("hello world %s" % abc)


if __name__ == '__main__':
    unittest.main()