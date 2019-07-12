#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
# post请求 有    1.post无参数和body  2.body有参数有body，body内容又分为有四种数据格式

import requests
import urllib3
urllib3.disable_warnings()

#   不带body的请求
# 接口文档地址：https://www.juhe.cn/docs/api/id/39
url = "http://v.juhe.cn/weather/index"
params = {
    "cityname": "上海",# 城市名或城市ID，如："苏州"，需要utf8 urlencode
    "dtype": "json",     # 返回数据格式：json或xml,默认json
    "format": "1",       # 未来7天预报(future)两种返回格式，1或2，默认1
    "key": "80b4d4e1d870d257d3344fcf2d08f64a"#  key是我个人申请的，群内学习使用，勿乱发
}
r = requests.post(url,params=params,verify=False)
print(r.status_code)



# -- application/json   --------------------这种就是传json参数  也可以用data参数处理：data=json.dumps(json)
# ---application/x-www-form-urlencode -------这种就是传data参数


# body为json数据格式  # content-type是申明body的数据类型
url="http://api.moiiee.com:9097/app/members/chandao"
headers={
'Content-Type':'application/json',
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0",
}
jsons ={"principalName":"18973019192","password":"yu1234","type":1}
r = requests.post(url,json=jsons,headers=headers)
print(r.status_code)
print(r.text)
# 也可以用data参数处理json数据格式
import json
r = requests.post(url,data=json.dumps(jsons),headers=headers)
print(r.status_code)
print(r.text)

# body为application/x-www-form-urlencoded数据格式
url="http://127.0.0.1:81/zentao/user-chandao.html"
headers={
'Content-Type':'application/x-www-form-urlencoded',
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0"
}
data ={
'account':'admin',
'password':'e10adc3949ba59abbe56e057f20f883e',
}
r = requests.post(url,data=data,headers=headers)
print(r.status_code)
print(r.text)

# body为xml格式
url = "http://www.example.com/"

body = '''
<?xml_ version=“1.0” encoding = “UTF-8”?>
<COM>
<REQ name="上海-悠悠">
<USER_ID>yoyoketang</USER_ID>
<COMMODITY_ID>123456</COMMODITY_ID>
<SESSION_ID>absbnmasbnfmasbm1213</SESSION_ID>
</REQ>
</COM>
'''
r = requests.post(url, data=body.encode("utf-8"))
print(r.text)