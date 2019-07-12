#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
import requests,re,urllib3
urllib3.disable_warnings()

# 会话 作用：缓存cokkies(自动保存，相当于浏览器)
# s = requests.session()
# url = "http://127.0.0.1:81/zentao/user-login.html"
# headers={
# 'Content-Type':'application/x-www-form-urlencoded',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
# }
# s.headers.update(headers)
# print(s.headers)
# # s.get(url,verify=False)
# body = {"account": "admin",
#         "password": "e10adc3949ba59abbe56e057f20f883e",
#         "referer": "",
#          "keepLogin[]": "on"
#         }
#
# r = s.post(url,data=body) # url, headers=h, data=body
# r = s.get("http://127.0.0.1:81/zentao/my/",verify=False)
# print(r.status_code)
# print(r.text)
# print(r.cookies)


# 绕过登录 获取登录的cookies去() 发后面的请求
# # 1 fiddler抓包到登录的cookies
# #
# s = requests.session()
# # 加cookies
# c = requests.cookies.RequestsCookieJar()
# # 登录后的cookies
# c.set("sid","l4fltimed0r382qk5fn9u7mmn4")
# # 更新s的cookies
# s.cookies.update(c)
# print(s.cookies)
# # 访问需要登录后才能访问的网站
# r = s.get("http://127.0.0.1:81/zentao/my/",verify=False)
# print(r.status_code)
# print(r.text)
# print(r.cookies)


#  token 有些网站的登录并不是采取cookie形式，而是用token 对比下登录前后的抓包，就知道是不是cookie登录了
# Token参数有时候会藏在头部，有时候带在url地址里， 有时候在body里，形式不固定




# 拉勾网实例  获取动态参数
s = requests.session()
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}
s.headers.update(headers)
url = "https://passport.lagou.com/chandao/chandao.html"
r = s.get(url,verify=False)
token = re.findall("window.X_Anti_Forge_Token = '(.+?)';",r.content.decode('utf-8'))[0]
code = re.findall("X_Anti_Forge_Code = '(.+?)';",r.content.decode('utf-8'))[0]

# 登录接口登录
url = 'https://passport.lagou.com/chandao/chandao.json'
headers = {
"X-Anit-Forge-Token":token,
"X-Anit-Forge-Code":code
}
data = {
"isValidate":"true",
"username":"18985591322",
"password":"29fb99f3c750e957b0da82e2eb3718c0",
"request_form_verifyCode":"",
"submit":"",
"challenge":"c2da63450789271160a3e84aaaa0cac4"
}
s.headers.update(headers)

r = s.post(url,data=data,verify=False)
print(r.text)


# 学信网登陆
import requests,re

s = requests.session()
url = "https://account.chsi.com.cn/passport/chandao"
headers={
'Content-Type':'application/x-www-form-urlencoded',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}
s.headers.update(headers)
print(s.headers)
r = s.get(url, verify=False)
jsessionid = s.cookies.get('JSESSIONID')
lt = re.findall("name=\"lt\" value=\"(.+?)\" />",r.text)[0]

url = ';'.join([url,jsessionid])
print(url)
body = {
    "username":	"18973019152",
    "password": "yu123456",
    "submit": "登录",
    "lt": lt,
    "execution": "e1s1",
    "_eventId":	"submit"
        }
#
r = s.post(url, data=body,verify=False)  # url, headers=h, data=body
print(r.text)
print(r.status_code)
print(r.cookies)