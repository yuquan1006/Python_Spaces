#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 14:55
# @Author  : Yuquan
# @Site    : 
# @File    : yaml02.py
# @Software: PyCharm
import yaml
import requests

# 读取yaml数据
f = open("./moiiee_login.yaml",encoding='utf-8')
cfg = f.read()
cfg = yaml.load(cfg)
print(cfg)

host = 'http://api.moiiee.com:9097'
for i in cfg:
    if isinstance(i,dict):
        headers = i.get('headers')
        print(headers)
        method = i.get('method')
        url = host+i.get('url')
        detail = i.get('detail')
        data = i.get('data')
        check = i.get('check')

        session = requests.session()
        session.headers.update(headers)
        if method == "post":
            result = session.post(url, json=data)
            print("正在测试%s"%detail)
            result = result.json()
            if result.get(check[0]):
                print("测试通过！")
            else:
                print("测试不通过！断言失败")
        else:print("~~暂时只支持post请求")
