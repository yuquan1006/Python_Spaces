import requests
import os
s = requests.session()
def login():
    ''' mes实名认证上传身份证接口-demo '''
    datas = '{"requestObj": {"loginName": "yu3@qq.com", "password": "123456yu"}}'
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    print(type(datas))
    response = s.post("http://mesnew1.innertest.ipaylinks.com/mes-gateway/api/security/login.json", data=datas, headers=headers)
    print(s.headers)
    s.headers.update({"AUTH-TOKEN":response.json()['responseObj']['token']})
    print(s.headers)

    files = {'file': (os.path.join(os.path.dirname(os.path.realpath(__file__)), "1.jpg"), open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "1.jpg"), 'rb'), "img/jpeg")}
    data ={"subPath": "auth"}
    response = s.post("http://mesnew1.innertest.ipaylinks.com/mes-gateway/api/file/upload.json", data=data, files=files)
    print(s.headers)

    print(response.status_code)
if __name__ == '__main__':
    # login()
    print(os.path.dirname(os.path.realpath(__file__)))
    print(os.path.join(os.path.dirname(os.path.realpath(__file__)), "1.jpg"))