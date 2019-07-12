#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
# 第一课 get请求
#  两种情况：1.get无参数 2.get有参数

# https://www.juhe.cn/
# 可以不用注册，用我申请的APPkey就行了
# 全国天气预报 AppKey：80b4d4e1d870d257d3344fcf2d08f64a
# 历史天气 AppKey：9b712c1b5a2ac854d587fdd7b7b349d7
# QQ号码测吉凶 AppKey：8dbee1fcd8627fb6699bce7b986adc45

import requests
# 使用这个方法就OK了urllib3.disable_warnings()  # 忽略警告
import urllib3
urllib3.disable_warnings()

# 1
url = "https://wwww.baidu.com"
# SSL验证 因为使用fiddler，所以要忽略掉ssl证书。但是会有警告
r = requests.get(url,verify=False)
print(r.status_code)
# print(r.text)


# 2 get请求有参数
url = 'http://v.juhe.cn/weather/index'
#  字典传入数据
params = {
"format":2,
"cityname":"苏州", # requests自动将中文转化成urlencode编码
"key":"80b4d4e1d870d257d3344fcf2d08f64a",
"dtype":"json"
}
# 列表/元祖 传入数据 当出现相同key值是字典就用不了 就用列表/元祖
params = [
["format",2],
["cityname","苏州"], # requests自动将中文转化成urlencode编码
["key","80b4d4e1d870d257d3344fcf2d08f64a"]
["dtype","json"]
]




# get请求 头部需要User-Agent伪造浏览器()，有的网站需要cookies
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0",
}
r = requests.get(url,params=params,headers=headers)
print(r.url)
# print(r.request.headers)
# print(r.status_code)
# print(r.headers)
# print(r.text)
# print(r.content)
# print(r.raw)
# print(r.json())


# 403 - Forbidden url和请求参数都对，却没权限，可能原因 1.服务器识别到你是代码请求的，防脚本机制– 解决办法：加 那就是需要身份验证了，如cookies
# Headers中少了cookies中场景    fidder抓包：浏览器请求和代码请求对比，发现少了cookies信息。

url = "http://zzk-s.cnblogs.com/s/blogpost"
headers={
"Cookie": "_ga=GA1.2.1359376775.1536840561; __gads=ID=096bf276296714e0:T=1539426005:S=ALNI_MaNdBnVlwmLdPd_qA6xz_Z9xrE6yA",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0"
}
r = requests.get(url,params=params,headers=headers)
print(r.status_code)

# Gzip解码
# 有些响应内容是gzip压缩的，text只能打印文本内容(会乱码)，用content是二进制流 --一般获取返回值内容，推荐用content
url = "https://wwww.baidu.com"
r = requests.get(url,verify=False)
# content解码成utf-8
print(r.text)
print(r.content.decode('utf-8'))


