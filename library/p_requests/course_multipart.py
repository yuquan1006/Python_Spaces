#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
#  multipart/form-data 1.文件上传  2.表单提交   这种数据格式不用header中contenttype
import requests,time
from requests_demo01.chandao_login import login
# 文件上传

def upload(s,filepath=r"C:\Users\Administrator\Desktop\1.png",filename="1.png",filetype="image/png"):

    url = "http://127.0.0.1:81/zentao/file-ajaxUpload.html?dir=image"
    files = {
        "localUrl": (None, filename),
        "imgFile": (filename, open(filepath, "rb"), filetype)
    }
    r = s.post(url, files=files)
    print(r.json())
    return r.json()['url']


# 表单上传  添加一般bug
def add_bug(s):
    url = "http://127.0.0.1:81/zentao/bug-create-2-0-moduleID=0.html"
    data = {
        "product":"1",
        "module":"0",
        "project":"",
        "openedBuild[]":"trunk",
        "assignedTo":"admin",
        "type":"codeerror",
        "os":"",
        "browser":"",
        "color":"",
        "title":"bug_title%s"%str(time.time()),
        "severity":"3",
        "pri":"0",
        "steps":'<img src="data/upload/1/201811/0420380406493ra0.png" alt="" /><p>[步骤]</p><p>[结果]</p><p>[期望]</p>',
        "story":"",
        "task":"0",
        "keywords":"",
        "files[]":"",
        "labels[]":"",
        "case":"0",
        "caseVersion":"0",
        "result":"0",
        "testtask":"0"
    }
    r = s.post(url,data=data)
    print(r.text)


# 表单+文件上传  添加附件的bug
def add_file_bug(s):
    url = "http://127.0.0.1:81/zentao/bug-create-2-0-moduleID=0.html"
    file = {
        "files[]": ("1.txt", open(r"C:\Users\Administrator\Desktop\1.txt", "rb"), "text/plain")
    }
    data = {
        "product":"1",
        "module":"0",
        "project":"",
        "openedBuild[]":"trunk",
        "assignedTo":"admin",
        "type":"codeerror",
        "os":"",
        "browser":"",
        "color":"",
        "title":"bug_title%s"%str(time.time()),
        "severity":"3",
        "pri":"0",
        "steps":'<img src="data/upload/1/201811/0420380406493ra0.png" alt="" /><p>[步骤]</p><p>[结果]</p><p>[期望]</p>',
        "story":"",
        "task":"0",
        "keywords":"",
        "files[]":"",
        "labels[]":"",
        "case":"0",
        "caseVersion":"0",
        "result":"0",
        "testtask":"0"
    }
    r = s.post(url, data=data, files=file)
    print(r.text)

# 多个附件
def add_files_bug(s):
    url = "http://127.0.0.1:81/zentao/bug-create-2-0-moduleID=0.html"
    file = [
        ["files[]", ("1.txt", open(r"C:\Users\Administrator\Desktop\1.txt", "rb"), "text/plain")],
        ["files[]",("1.png", open(r"C:\Users\Administrator\Desktop\1.png", "rb"), "image/png")]
    ]
    data = {
        "product":"1",
        "module":"0",
        "project":"",
        "openedBuild[]":"trunk",
        "assignedTo":"admin",
        "type":"codeerror",
        "os":"",
        "browser":"",
        "color":"",
        "title":"bug_title%s"%str(time.time()),
        "severity":"3",
        "pri":"0",
        "steps":'<img src="data/upload/1/201811/0420380406493ra0.png" alt="" /><p>[步骤]</p><p>[结果]</p><p>[期望]</p>',
        "story":"",
        "task":"0",
        "keywords":"",
        "files[]":"",
        "labels[]":"",
        "case":"0",
        "caseVersion":"0",
        "result":"0",
        "testtask":"0"
    }
    r = s.post(url, data=data, files=file)
    print(r.text)

# 导入requests-toolbelt 模块处理
from requests_toolbelt import MultipartEncoder
def add_file_bug_01(s):
    url = "http://127.0.0.1:81/zentao/bug-create-2-0-moduleID=0.html"

    data = {
        "product":"1",
        "module":"0",
        "project":"",
        "openedBuild[]":"trunk",
        "assignedTo":"admin",
        "type":"codeerror",
        "os":"",
        "browser":"",
        "color":"",
        "title":"bug_title%s"%str(time.time()),
        "severity":"3",
        "pri":"0",
        "steps":'<img src="data/upload/1/201811/0420380406493ra0.png" alt="" /><p>[步骤]</p><p>[结果]</p><p>[期望]</p>',
        "story":"",
        "task":"0",
        "keywords":"",
        "files[]":"",
        "labels[]":"",
        "case":"0",
        "caseVersion":"0",
        "result":"0",
        "testtask":"0",
        "files[]": ("1.txt", open(r"C:\Users\Administrator\Desktop\1.txt", "rb"), "text/plain")
    }
    m = MultipartEncoder(fields=data)
    r = s.post(url, data=m, headers={'Content-Type': m.content_type})
    print(r.text)


if __name__ == '__main__':
    s = requests.session()
    login(s)
    upload(s)
    add_bug(s)
    # add_file_bug(s)
    # add_files_bug(s)
    # add_file_bug_01(s)