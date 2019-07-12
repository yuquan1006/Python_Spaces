#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 18:02
# @Author  : Yuquan
# @Site    : 
# @File    : mock_server.py
# @Software: PyCharm

'''         mock-server 环境搭建
mock-server 用途就是开发在开发的过程中，需要依赖一部分的接口，但是对方
没有提供或者环境等等情况

mock开源框架：
简单来说，Moco就是解决了开发前端时没有后端支持，开发接口时依赖没有到位的尴尬场景。当然Moco的灵活性，让其有越来越多的应用场景。
moco的安装非常简单，官网下载jar包https://github.com/dreamhead/moco ，在同目录下创建一个foo.json配置文件，
命令行：java -jar moco-runner-0.12.0-standalone.jar http -p 12306 -c foo.json，然后浏览器输入http://localhost:12306 即可看到响应
moco 文档：https://github.com/dreamhead/moco/blob/master/moco-doc/apis.md
moco，可以设置request，response，headers,uri等，还可以使用rediectTo设置URL重定向

'''

# test.json
'''[
    {
        "request":
        {
            "uri":"/test01"
        },
        "response":
        {
            "text":"hello world",
        "headers":
        {
            "SelfHeader":"SelfHeader"
        }
        }
    },

    {
        "request":
        {
            "uri":"/test"
        },

        "redirectTo":"http://www.baidu.com"
    }


]'''
