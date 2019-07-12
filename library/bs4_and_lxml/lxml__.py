#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 9:18
# @Author  : Yuquan
# @Site    : 
# @File    : lxml__.py
# @Software: PyCharm
from lxml import html
import re, requests
import urllib3
urllib3.disable_warnings()
etree = html.etree

html = '''
<meta charset="UTF-8"> <!-- for HTML5 -->
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<html>
<head><title>yoyo ketang</title></head>
<body>
<b><!--Hey, this in comment!--></b>
<p class="title"><b>yoyoketang</b></p>
<p class="yoyo">这里是我的微信公众号：yoyoketang
<a href="http://www.cnblogs.com/yoyoketang/tag/fiddler/" class="sister" id="link1">fiddler教程</a>，
<a href="http://www.cnblogs.com/yoyoketang/tag/python/" class="sister" id="link2">python笔记</a>,
<a href="http://www.cnblogs.com/yoyoketang/tag/selenium/" class="sister" id="link3">selenium文档</a>;
快来关注吧！</p>
<p class="story">...</p>
</body>
</html>
'''

# 解析html内容
demo = etree.HTML(html)
print(demo)

# 打印解析内容的str
str = etree.tostring(demo, encoding="utf-8", pretty_print=True)
# print(str.decode("utf-8"))

# xpath定位
# 一次定到
a = demo.xpath("//*[@class=\"yoyo\"]")
print(a)
# 获取文本
t = a[0].text
print(t)

# 多次定位
a = demo.xpath("//*[@class=\"yoyo\"]")
b = a[0].xpath("//*[@id='link2']")
print(b[0].text)
print(b[0].get('class'))

# 获取当前节点标签
b = a[0].xpath("//*[@id='link2']")
print(b[0].tag)

# 获取当前节点文本信息
print(b[0].text)

# 获取当前节点元素全部属性（dict格式）
print(b[0].attrib)
print(b[0].attrib['href'])

# 获取当前节点某个属性值
print(b[0].get('id'))

# 所有子节点
for i in a[0].iter():
    print(i.text)

#获取当前节点下全部文本
print(a[0].xpath("text()"))

# 获取父节点
print(b[0].getparent().tag)















# 学信网登录案例




s = requests.session()

result = {}
loginurl = "https://account.chsi.com.cn/passport/chandao"
h1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
}
s.headers.update(h1)
r = s.get(loginurl, verify=False)

# print(r.content.decode("utf-8"))
# lt = re.findall('name="lt" value=\"(.+?)\"', r.content.decode("utf-8"))[0]
dom = etree.HTML(r.text)
lts = dom.xpath("//input[@name=\"lt\"]")
print(lts)
lt = lts[0].get('value')
print("取出lt的值：%s" % lt)
# execution = re.findall('name=\"execution\" value=\"(.+?)\"', r.content.decode("utf-8"))[0]
# print("取出execution的值：%s" % execution)

#
# h2 = {
#     "Referer": loginurl,
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
#     "Accept": "text/html,application/xhtml+xml_,application/xml_;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     "Origin": "https://account.chsi.com.cn",
#     "Content-Length": "119",
#     "Cache-Control": "max-age=0",
#     "Upgrade-Insecure-Requests": "1",
#     "Content-Type": "application/x-www-form-urlencoded"
#     }
# body = {
#     "username": "33333333",  # 出现验证码时候，账号要改下
#     "password": "1111111",
#     "rememberMe": "true",
#     "lt": lt,
#     "execution": execution,
#     "_eventId": "submit"
# }
# s.headers.update(h2)
# r4 = s.post(loginurl, data=body, verify=False)
# # print(r4.text)
#
# # 提取登录结果提示语
# try:
#     errors = re.findall("<div class=\'ct_input errors\'>(.+?)</div>", r4.text)
#     print("请改了账号再提交，系统锁定账号密码错误次数了：%s"%errors[0])
# except IndexError:
#     error = re.findall('<div id="status" class="errors">(.+?)</div>', r4.text)
#     print("密码不对：%s"%error[0])
# except:
#     print("其它原因：！！！！！！！！！！")
#     print(r4.text)
#
