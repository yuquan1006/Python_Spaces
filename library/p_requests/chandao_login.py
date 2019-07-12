#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
import requests

def login(s,username="admin",passwd="e10adc3949ba59abbe56e057f20f883e"):

    url = "http://127.0.0.1:81/zentao/user-chandao.html"
    headers = {
        "Content - Type": "application / x - www - form - urlencoded",
        "User - Agent": "Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 68.0.3440.75 Safari / 537.36"
    }
    data = {
        "account": username,
        "password": passwd,
        "referer": ""
    }


    r = s.post(url,headers=headers,data=data,verify=False)
    # print(r.status_code)
    # print(r.content.decode("utf-8"))
    return r.content.decode("utf-8")

def is_login_success(result):
    if "登录失败" in result:
        print( "登录失败！")
        return False
    elif "parent.location=" in result:
        print("登录成功！")
        return True
    else:
        print("出现了其它的返回结果，登录失败！")
        return False


if __name__ == '__main__':
    s = requests.session()
    # 参数化
    result = login(s, "admin", "e10adc3949ba59abbe56e057f20f883e")
    # 判断登录结果
    result = is_login_success(result)
    print('测试结果是:%s'%result)
