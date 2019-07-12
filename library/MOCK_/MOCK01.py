#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 14:35
# @Author  : Yuquan
# @Site    : 
# @File    : MOCK01.py
# @Software: PyCharm

def zhifu():
    '''假设这里是一个支付的功能, 未开发完
    支付成功返回：{"result": "success", "reason": "null"}
    支付失败返回：{"result": "fail", "reason": "余额不足"}'''
    pass

def zhifu_status():
    '''根据支付的结果 success or fail，判断跳转到对应页面'''
    result = zhifu()
    print(result)
    try:
        if result['result']=="success":
            return "支付成功"
        elif result['result']=="fail":
            return "支付失败"
        else:
            return "未知失败"
    except:
        return "Error, 服务端返回异常!"