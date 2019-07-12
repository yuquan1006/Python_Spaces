import dubbo_telnet


host = '47.100.10.132' # Doubble服务器IP
port = '2181'  # Doubble服务端口
# 初始化dubbo对象
conn = dubbo_telnet.connect(host,port)
# 设置telnet连接超时时间
conn.set_connect_timeout(10)
# 设置dubbo服务返回响应的编码
conn.set_encoding('gbk')
# 显示服务列表
print(conn.do("ls".encode('utf-8')))

interface = 'com.ipaylinks.acct.facade.AccountManageFacade'.encode('utf-8')
method = 'openAccount'.encode('utf-8')
param = [{"memberCode": "20000001520", "memberType": "1", "accountIdentity": "9527", "accountType": "320299","currencies": "USD"}]
print(conn.invoke(interface, method, param))
command = 'invoke %s.%s(%s)' % (interface, method, param) # command  = 'invoke' dubbo服务名.方法名（参数）
print(conn.do(command))

