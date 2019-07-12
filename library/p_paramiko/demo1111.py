'''连接SSh命令行工具'''
import paramiko
hostInfo_list=[]
def main():
    print('''----------------- SSH【Menu】 -----------------
<1>Connect a host
<2>Add host
<3>Remove host
-----------------------------------------------''')
    while 1:
        chosee = input("Please select depend on tips:")
        if int(chosee)==2:
            add_host()
        elif int(chosee)==1:
            connect_to_host()
        elif int(chosee)==3:
            delete_host()


def add_host():
    '''添加主机信息到list'''
    host_name =input("Input host:")
    port_name =input("Input port:")
    username_name =input("Input username:")
    password_name =input("Input password:")
    other_name =input("Input other_name:")
    host_dict={}
    host_dict['host'] = host_name
    host_dict['port'] = port_name
    host_dict['username_name'] = username_name
    host_dict['password_name'] = password_name
    host_dict['other_name'] = other_name
    global hostInfo_list
    hostInfo_list.append(host_dict)
    print("添加成功！")
    print(hostInfo_list)
def delete_host():
    print(hostInfo_list)
    otherName = input('input remove otherName:')
    flag = input('are you true remove {} 【y/n】'.format(otherName))
    if flag=='y':
        for i in hostInfo_list:
            if i['other_name']==otherName:
                hostInfo_list.remove(i)
                print('Remove Sucessful!')

def ppp():
    print("现在host_list：")
    global hostInfo_list
    print(hostInfo_list)
def connect_to_host():
    otherName = input("Input other_name：")
    print(hostInfo_list)
    for i in hostInfo_list:
        for j in i.values():
            if otherName == j:
                # 实例化SSHClient
                client = paramiko.SSHClient()
                # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                # 连接SSH服务端，以用户名和密码进行认证
                client.connect(hostname=i['host'], port=i['port'], username=i['username_name'], password=i['password_name'])
                while 1:
                    enter = open("Enter the Command:")
                    if enter!='q':
                        # 打开一个Channel并执行命令
                        stdin, stdout, stderr = client.exec_command(enter)  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
                        # 打印执行结果
                        print(stdout.read().decode('utf-8'))
                    else:
                        break


if __name__ == '__main__':
    main()


