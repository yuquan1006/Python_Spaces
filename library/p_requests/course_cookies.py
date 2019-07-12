#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6

import requests
import urllib3
urllib3.disable_warnings()
from urllib.parse import parse_qsl
import re

# cookies
# 大数据杀熟

# 1.Cookie在重定向后url上
url = "http://zzk-s.cnblogs.com/s/blogpost"
# r = requests.get(url, verify=False)
# # 第1种情况，cookie在重定向后的url上
# res_url = r.url
# print(res_url)   # 重定向后cookie在url的头部了
# canshu = res_url.split("?")[1]  # 获取问号后面的参数
# # 获取cookies,转字典
# cook = dict(parse_qsl(canshu))
# print(cook)
# # cookies传入
# par = {"Keywords": "yoyo"}
# r2 = requests.get(url, cookies=cook)
# print(r2.text)

# Requests会自动处理重定向请求，返回的是最后一次请求的response对象  禁用重定向 allow_redirects=False


# 2.Cookie在重定向前的返回正文中
# r = requests.get(url, verify=False,allow_redirects=False)
# content = r.text
# # 正则提取
# value = re.findall("/blogpost\?(.+?)\">here",content)[0]
# print(value)
# # 将a=b格式转化成字典类型
# cook = dict(parse_qsl(value))
# print(cook)
#
# # cookies传入
# r = requests.get(url,cookies=cook,verify=False)
# print(r.status_code)
# print(r.text)

# 3.cookies在返回的头部 例如 下一个请求的cookies在上一个请求的返回头部里
# r = requests.get(url, verify=False,allow_redirects=False)
# print(r.headers)
# cook = r.headers['Set-Cookie']
# # Cookies可以单独作为一个参数传入，也可以放到头部，作为头部的一个Cookie参数
# # （两种方法都可以）
# headers ={"Cookie":cook}
# r = requests.get(url,headers=headers,verify=False)
# print(r.status_code)
# print(r.text)

# 重定向
# 1.fiddler抓包 可以看到重定向的地址在response的headers里Location参数会告诉指向下一地址

# 2.重定向的请求历史  History获取的是一个list列表，list里面对象是请求的一次会话
# r = requests.get(url, verify=False)
# print(r.history)
# for i in r.history:
#     print(r.status_code)
#     print(r.url)

# 禅道登录案例

headers={
'Content-Type':'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'

}

# 将cookies传入下一个请求
body = {"account": "admin",
        "password": "e10adc3949ba59abbe56e057f20f883e",
        "referer": "",
        "keepLogin[]": "on"
        }
headers={
'Content-Type':'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'

}
r = requests.post("http://127.0.0.1:81/zentao/user-chandao.html",headers=headers,data=body) # url, headers=h, data=body
print(r.headers)
cook = dict(r.cookies)
print(cook)
r = requests.get("http://127.0.0.1:81/zentao/my/",cookies=cook,verify=False)
print(r.status_code)
print(r.text)

# 总结三种传入cookies方法
'''
1.头部传入Cookie:XX
2.在请求中加参数cookies=字典类型
3.直接传入requescookieJar    r.cookies
'''
