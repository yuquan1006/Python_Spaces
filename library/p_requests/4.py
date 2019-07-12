#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6

import requests
r = requests.session()
headers = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
r.headers.update(headers)
g_login_url = "http://127.0.0.1:81/zentao/user-login.html"
response = r.get(g_login_url)
# print(response.text)
headers = response.headers
# cookies = headers['Set-Cookie']
# headers = {'Cookie':cookies}
# print(headers)
# r.headers.update(headers)
print(r.headers)

# login_url = "http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html"
# cookies = {}
# data = {"account":"admin","password":"e10adc3949ba59abbe56e057f20f883e"}
# # r.headers.update(headers)
# # r.cookies.set()
# response = requests.post(login_url,data=data,headers=headers)
# print(response.text)
# print(response.cookies)
# cookies = response.cookies
#
# url = "http://127.0.0.1:81/zentao/my-profile.html?onlybody=yes"
# response = requests.get(url,cookies=cookies)
# print(response.text)
#
#
# loginout_url = "http://127.0.0.1:81/zentao/user-logout.html "
# response = requests.get(loginout_url,cookies=cookies)
# print(response.status_code)
# print(response.text)
#
