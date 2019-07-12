import json
import socket
import telnetlib
class Dubbo(telnetlib.Telnet):
    prompt = 'dubbo>'
    coding = 'utf-8'
    def __init__(self, host=None, port=0, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        super().__init__(host, port)
        self.write(b'\n')
    def command(self, flag, str_=""):
        data = self.read_until(flag.encode())
        self.write(str_.encode() + b"\n")
        return data
    def invoke(self, service_name, method_name, arg):
        command_str = "invoke {0}.{1}({2})".format( service_name, method_name, json.dumps(arg))
        self.command(Dubbo.prompt, command_str)
        data = self.command(Dubbo.prompt, "")
        data = data.decode(Dubbo.coding,errors='ignore').split('\n')[0].strip()
        return data
    def do(self, arg):
        command_str = arg
        self.command(Dubbo.prompt, command_str)
        data = self.command(Dubbo.prompt, command_str)
        data = data.decode(Dubbo.coding,errors='ignore').split('\n')[0].strip()
        return data
if __name__ == '__main__':
    host = '172.16.1.15'  # Doubble服务器IP
    port = 20203  # Doubble服务端口
    interface = 'com.ipaylinks.acct.facade.AccountManageFacade'
    method = 'openAccount'
    param = ''
    conn = Dubbo(host, port) #格式invoke 接口全名字.方法名(参数1，参数2，参数3...参数n)
    param = [{"memberCode":"20000001520","memberType":"1","accountIdentity":"9527","accountType":"320299","currencies":"USD"}]
    command = 'invoke %s.%s(%s)' % (interface, method, param)  # command  = 'invoke' dubbo服务名.方法名（参数）
    print(conn.do(command))