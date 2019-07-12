#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 14:02
# @Author  : Yuquan
# @Site    : 
# @File    : python设计模式_工厂模式.py
# @Software: PyCharm

class Moxing(object):
    '''模型类'''
    def __init__(self,name=''):
        self.name = name
    def shuoming(self):
        pass
        # print('我是{0}模型'.format(self.name))

class Zhegnfangxing(Moxing):
    '''正方形'''
    def __init__(self, name):
        '''继承父类的构造方法,super(子类，self).__init__(参数1，参数2，....)'''
        super(Zhegnfangxing,self).__init__(name)
        self.name = name

    def shuoming(self):
        print('我是{0}模型'.format(self.name))

if __name__ == '__main__':
    a = Moxing()
    b = Zhegnfangxing(name='正反行')
    a.shuoming()
    b.shuoming()