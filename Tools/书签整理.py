# -*- coding:utf-8 -*-
import re,os,sys


strat_Str ='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>书签</title>
</head>
<body>
    <H1>书签</H1>
'''
end_Str='''</body>
</html>'''
def readBookMark(fileName):
    '''读取书签文件中的url
    :return 返回超链接中文本和host
    '''
    link_list = []
    host_dict = {}
    linkName_list=[]
    link_dict= {}

    try:
        with open(fileName,'rb') as f:
            i = f.read().decode('utf-8')
            # print(i)
            link_list = re.findall("<DT><A HREF=\"(.+?)\"",i) # 获取url
            linkName_list = re.findall("\">(.+?)</A>",i)  # 获取便签内文本
            for l in range(len(link_list)):
                # 组合url和文本
                link_dict[linkName_list[l]] =  link_list[l]
            # print(link_dict)
            # print(link_list)
            for k,v in link_dict.items():
                # 获取host，并组合文本和host
                result = re.findall(r"http://.*?\.com/|http://.*?\.cn/|https://.*?\.com/|https://.*?\.cn/|https://.*?\.net/|http://.*?/",v)
                if result:
                    host_dict[k] = result[0]
    except BaseException as e:
        print("error！读取{}书签文件失败，可能原因：e".format(fileName))

        # print('*************')
            # print(host_list)
    return host_dict



def readCsv(fileName):
    '''读取csv文件，获取host，用户名，密码'''
    host_list = []
    user_list = []
    pwd_list = []
    all_list=[]
    try:
        if not os.path.exists(fileName):
            print("error！读取{}密码文件失败，可能原因：文件不存在".format(fileName))
            sys.exit(500)
        with open(fileName,"rb") as f:
            for num,i in enumerate(f.readlines()):
                if num != 0:
                    # print(i.decode('utf-8'),end='')
                    split_list = i.decode('utf-8').split(',')
                    # print(split_list)
                    host_list.append(split_list[0])
                    user_list.append(split_list[2])
                    pwd_list.append(split_list[3][:-2])
        print(host_list)
        all_list.append(host_list)
        all_list.append(user_list)
        all_list.append(pwd_list)
    except IOError as e:
        print("error！读取{}密码文件失败，可能原因：文件内容为空\n e".format(fileName))
    except BaseException as e:
        print("error！读取{}密码文件失败，可能原因：e".format(fileName))
    return all_list

def check(host_dict,all_list):
    write_list = []
    try:
        for k,v in host_dict.items():
            for num,j in enumerate(all_list[0]):
                if j in v:
                    print("书签名：{}，书签host：{}，Csv文件host:{},用户名：{}，密码：{}".format(k,v,j,all_list[1][num],all_list[2][num]))
                    strs = "<a href=\"{}\">{}</a> <sapn>用户名：{} 密码：{} </sapn><br>".format(v, k, all_list[1][num],all_list[2][num])
                    write_list.append(strs.encode('utf-8'))
                    print(strs)
                else:
                    pass
    except BaseException as e:
        print("error！解析组装列表失败，可能原因：e")

    return write_list

def writeHtml(pwdFileName,bookMarksName,):
    try:
        a = readCsv(pwdFileName)
        print(a)
        b = readBookMark(bookMarksName)
        print(b)
        write_fileName = r"C:\Users\Skye\Desktop\关联书签密码.html"
        with open(write_fileName,"wb+") as f:
            f.write(strat_Str.encode('utf-8'))
        with open(write_fileName, "ab+") as f:
            f.writelines(check(b,a))
            f.write(end_Str.encode('utf-8'))
    except BaseException as e:
        print("error！写入文件失败，可能原因：",e)
    print("书签关联密码文件生成在{}".format(write_fileName))



def main():
    shuqian_input = input("请输入浏览器导出书签文件路径:")
    pwd_input = input("请输入浏览器导出密码文件路径:")
    writeHtml(pwd_input,shuqian_input)
    # writeHtml(r"C:\Users\Skye\Desktop\1.csv",r"C:\Users\Skye\Desktop\1.html")

if __name__ == '__main__':
    # a = readCsv(r"C:\Users\Skye\Desktop\Chrome密码 .txt")
    # # print(a)
    # # for i in a[0]:
    # #     print(i,end=', ')
    # # print('')
    # b = readBookMark(r"C:\Users\Skye\Desktop\谷歌书签.html")
    # # print(b)
    # check(b,a)
    # writeHtml("C:\Users\Skye\Desktop\")
    # print(os.path.exists(r'C:\Users\Skye\Desktop\1.html'))
    main()

    # 功能：请浏览器导出书签和浏览器导出密码匹配，写入到html文件。
