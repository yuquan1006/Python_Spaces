from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import re,requests,os

def getSignToLocal(name):
    '''
    根据输入姓名获取签名照片到本地
    :param name:姓名
    :return:null
    '''
    s = requests.Session()
    url = "http://www.uustv.com/";
    headers ={"Content-Type":"application/x-www-form-urlencoded",
              "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
    data = {"word":name,
    "sizes":"60",
    "fonts":"jfcs.ttf",
    "fontcolor":"#000000"}
    r = s.post(url,headers=headers,data=data)
    r.encoding ='utf-8'
    result = re.findall('<div class="tu">﻿<img src="(.+?)"/></div>',r.text)[0];
    url2 = url+result
    result = s.get(url2)
    parParh = os.path.dirname(os.path.realpath(__file__))
    with open("1.gif","wb") as f:
        f.write(result.content)
    choosepic()

def choosepic():
    '''
    打开本地获取的图片到窗口
    '''
    img_open = Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)),"1.gif"))
    img=ImageTk.PhotoImage(img_open)
    l2.config(image=img)
    l2.image=img


root = Tk()
root.title("个性签名")
# 设定窗口的大小，(长 * 宽)
root.geometry('500x300')
l1 = Label(root, text="姓名：")
l1.pack()
name_text = StringVar()
# 创建文本框
entry_text = Entry(root, width=30,)
entry_text.pack()
button = Button(root, text='开始', font=('Arial', 12), width=8, height=1,
                        command=lambda: getSignToLocal(entry_text.get())).pack()
l2 = Label(root)
l2.pack()
root.mainloop()