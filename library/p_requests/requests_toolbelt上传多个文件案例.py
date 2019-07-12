#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 17:40
# @Author  : Yuquan
# @Site    : 
# @File    : requests_toolbelt上传多个文件案例.py
# @Software: PyCharm
from requests_toolbelt import MultipartEncoder
import requests
import time

'''在当前脚本同一目录，放两张图片,取名：
yoyo1.jpg
yoyo2.jpg
'''

host = "http://127.0.0.1/"

def login(s, user="admin", psw="e10adc3949ba59abbe56e057f20f883e"):
    # s = requests.session()
    url = host+"zentao/user-chandao.html"
    h = {"Content-Type": "application/x-www-form-urlencoded",
        }
    body = {"account": user,
            "password": psw,
            "referer": host+"zentao/my/",
            "keepLogin[]": "on",
            }
    r = s.post(url, headers=h, data=body)
    print(r.status_code)
    # print(r.text)  # 如果.text出现乱码
    print(r.content.decode("utf-8"))
    return r.content.decode("utf-8")

def is_login_success(result):
    if "parent.location=" in result:
        print("登录成功！")
        return True
    elif "登录失败，请检查您的用户名或密码是否填写正确" in result:
        print("登录失败，用户名或密码不对")
        return False
    else:
        print("登录失败，其它问题：%s" % result)
        return False


def send_file_and_bug(src_img=""):
    '''
    f = (
            ("files[]", (filename, open(jpgpath, "rb"), filetype)),
            ("labels[]",  (None, "yoyo1")),
            ("files[]", (filename, open(jpgpath, "rb"), filetype)),
            ("labels[]",  (None, "yoyo2"))
        )
    '''
    # bug正文图片地址，如：/zentao/data/upload/1/201811/04202727017659eh.jpg
    src = src_img
    url = host+"zentao/bug-create-1-0-moduleID=0.html"
    timestrp = str(time.time())
    body = (
        ("product", "1"),
        ("module", "0"),
        ("project", ""),
        ("openedBuild[]", "trunk"),
        ("assignedTo", "admin"),
        ("type", "codeerror"),
        ("os", "all"),
        ("browser", "all"),
        ("color", ""),
        ("title", "requests_toolbelt上传的附件111_%s"%timestrp),
        ("severity", "3"),
        ("pri", "0"),
        ("steps", '<p>[步骤]</p>\
                <p>1、第一步点</p>\
                <p>2、第二步点</p>\
                <p>3、点三步点</p>\
                <p>[期望]222<img src="%s" alt="" /></p>\
                <p>[结果]</p>\
                <p>[期望]</p>'%src),
        ("story", "0"),
        ("task", "0"),
        ("mailto[]", ""),
        ("keywords", ""),
        ("uid", "5a2955c884f98"),
        ("case", "0"),
        ("caseVersion", "0"),
        ("result", "0"),
        ("testtask", "0"),
        # f = 里面内容合并进来
        ("labels[]", (None, "yoyo1")),
        ("files[]", ("yoyo1.png", open("yoyo1.jpg", "rb"), "image/jpeg")),
        ("labels[]", (None, "yoyo2")),
        ("files[]", ("yoyo2.jpg", open("yoyo2.jpg", "rb"), "image/jpeg")),
        )
    m = MultipartEncoder(
         fields=body
    )
    r2 = s.post(url, data=m, headers={'Content-Type': m.content_type})
    print(r2.text)

if __name__ == '__main__':
    s = requests.session()
    login(s)
    send_file_and_bug()


