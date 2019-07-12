#!/usr/bin/python
#author         :YUQUAN
#projectName    :huice_base
#date           :
#version        :PYTHON3.6
#File           :Func.py
# 函数

# 编程 小驼峰：
# 类名、文件名首字母大写 每个单词首字母大写
# 方法名 首字母小写之后单词首字母大写

# 系统内置函数
#abs（-1）绝对值
#len（list）序列长度
#sum（[1,2,3）、min([23,3,3]) 最大最小值
#round() 四舍五入
# 类型转化 float() 浮点数 int（）、str（）
# type() 查看数据类型
# 匿名函数 Lamada
func = lambda x,y:x+y
# print(func(1,4))
# func = func1
def func1(a,b):
    return a+b
# print(func1(1, 2))

# 函数说明
def add(a,b):
    '''
    两数相加函数，返回a+b的值
    :param a:
    :param b:
    :return: a+b的值
    '''
    return a+b
# print(add.__doc__)
# print(add(1,2))



# 参数个数不对，python解释器会自己检查出来，并抛出TypeError，但是参数类型不对，Python解释器就无法帮我们检查
# 我们可以使用isinstance()，对数据类型检查可以用内置函数isinstance()实现

# 练习：请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
def to_hex(value):
    try:
       if not isinstance(value,(int,)):
           # print('参数类型错误，应该为INT类型')
           raise TypeError("bad operand type")
       result = hex(value)
       return result
    except:
        raise
print(to_hex(123))


# 参数
#1 不指定参数名
def my_func(a,b):
    print(a,b)
# my_func('yuquan',1)

# 2 指定参数名 name,age
def my_func1(name,age):
    print('姓名：{name} 年龄：{age}'.format(name=name,age=age))
# 指定与不指定区别如下
# my_func1(23,'yuquan')
# my_func1(name='yuquan',age='23')

# 3 使用默认值  默认age = 18  （默认值参数在后，前面的参数必填参数）
def my_func2(name,age=18):
    print('姓名：{0} 年龄：{1}'.format(name,age))
# my_func2('yuquan')

# 有默认值的参数后不可再写必填参数
# def myfunc3(age=18,name):
#     print('姓名：{0} 年龄：{1}'.format(name, age))
# 会报错，应为’titia‘参数不知道给age还是name
# myfunc3('titia')

# 练习 小学入学函数
def small_school(name,gender,age=6,city='shanghai'):
    print("姓名：%s 年龄：%s 性别：%s 城市：%s"%(name,age,gender,city))
# small_school('小小',2,7,'shanghai')
# small_school(name='天天', gender=1)

# 练习
# 解析：因为list是可变数据类型，内存地址不会变，当list1掉用函数是默认参数空列表+10，内存列表为[10]
# 当再次调用时会使用内存列表[10].append('abc') 结果为[10, 'abc']
def extendList(val,a=[]):
    a.append(val)
    return a

list1=extendList(10)
# print(list1)
list2=extendList(1234,[])
# print(list2)
list3=extendList('abc')
# print(list3)

# 解决办法  定义默认参数要牢记一点：默认参数必须指向不变对象！
def extendList(val, list=None):
    if list is None:
        list =[]
    list.append(val)
    return list

# 可变参数  *参数在函数内部当做元祖处理
def my_check(name,age=1,*other):
    for i in other:
        print(i)
    print("必填参数是%s 默认参数是%s 其他参数是%s"%(name,age,other))
# my_check('ff',4,55,98)
# 练习 给定一组数字a，b，c……，请计算a2 + b2 + c2 +
def calc(num):
    s = 0
    for i in num:
        s += i ** 2
    return s
# print(calc([1,2]))

def calc(*num):
    s = 0
    for i in num:
        s += i ** 2
    return s
# print(calc(1,2,3))


# 可变参数  **参数在函数内部当做字典处理
def my_check1(name,age=1,**other):
    for i in other:
        print(i)
    print("必填参数是%s 默认参数是%s 其他参数是%s"%(name,age,other))
# my_check1('yuquan',21,city="shanghai",address="xihuanlu")
# 之间传入字典可以，但是在函数调用时对字典钱加**，告诉函数我传入的是字典
dic = {"address":"xihuanlu"}
# my_check1('yuan',24,**dic)

# 函数参数的顺序 必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# 总结：可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict



# 返回 return
# 1 函数遇到return 就结束
#　2 不写return 返回值为None
# 3 返回多个值 其实返回的是一个值 一个元祖
def a():
    return 0,1
print(a())          # a()函数返回的一个值。数据结构为元祖，不是两个值
(a,b)=a()           # 用一个元祖来接收a()函数返回的值 既 (a,b)=(0,1)
# print(a,b)

# def my_print():
#     '''
#     根据输入的值打印在一个盒子里 ，根据输入的值的大小
#     :return: None
#     '''
#     some = input("Enter ：")
#     changdu = 80
#     text = len(some)
#     box = text+6
#     kong_changdu = (changdu - box)//2
#     print(" "*kong_changdu+"+"+"-"*text+"+")
#     print(" "*kong_changdu+"|"+" "*text+"|")
#     print(" "*kong_changdu+"|"+some+"|")
#     print(" "*kong_changdu+"|" + " " *text+ "|")
#     print(" "*kong_changdu+"+" + "-" *text +"+")
# my_print()

# 练习 定义一个函数生成一个完成的get请求地址 http://192.168.0.199/app/demo?key=value  domain =主机 url =主机 data =参数
def get(domain,url=None,data=None):
    '''
    生成一个完成的get请求地址
    :param domain: 主机
    :param url: 路径可以不传
    :param data: 参数也可以不传
    :return: get请求地址
    '''
    result = "http://"+domain
    if url:
        result = result+url
    if data:
        list=[]
        for i,j in data.items():
            list.append(i+'='+j)
        result = result + "?" + "&".join(list)
    return result
# print(get("192.168.0.199",url="/app/demo",data={"uesrname":"yuquan"}))

# 递归函数 再函数内部在调用本身
# 阶乘 5！=1*2*3*4*5
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)
# print(fact(4))

# 回声     输入我爱你，打印的我爱你每次减少第一个：我爱你 爱你 你
# 循环实现
# a = input("enter:")
# while len(a)>0:
#     print(a)
#     a = a[1:]
#递归实现
# def fact_voice(context):
#     if len(context)==0:
#         return
#     print(context)
#     context = context[1:]
#     fact_voice(context)
# fact_voice(u"我爱你北京天安门")


def f(value):
    return value*0
print(list(map(f,[1,5,9,6,8,4])))
print(list(map(str,[1,5,8])))







# 高阶函数 函数的参数是函数
def add(a,b,f):
    return f(a)+f(b)
# 1 定义函数
def f(x):
    return x**2
print(add(1,3,f))
# 2 使用lambda，不需要再定义函数
add(a,b, lambda x:x**2)
print(add(2,3,f))

# map函数 接收两个参数，一个是函数，一个是序列
# 将传入的函数作用到序列的每一个元素中，并将结果作为一个iterators返回。用list（）转成list
# 基础解法
a = [1,2,3,4,5]
list1 = []
for i in a:
    list1.append(i**2)
print(list)
# 利用map函数解
b=list(map(lambda x:x**2,a))
print(b)

name = 'yuquan'
list_name=map(lambda x:x+'Y',name)
print(type(list_name))

#  利用map函数，将用户输入的不规范的英文名，变成首字母大写，其他字母小写的规范名字
list_name =['adam', 'LISA', 'barT']

newlist=list(map(lambda x:x.capitalize(),list_name))
print("+-+-+---")
a ='s'

print(newlist)

# filter 筛选函数 接收一个返回布尔值的函数和一个序列,传入的函数依次作用在序列每个元素上,根据返回值决定是保留还是丢弃
a = range(0,11)
a = list(filter(lambda x:x%2==0,a))

print(a)

# reduce函数 把一个函数作用在一个序列上，这个函数必须接受两个参数，reduce把结果和继续的序列的下一元素做累积计算
from functools import reduce
def cdd(x,y):
    return x+y
c= reduce(lambda x,y:x+y,[1,2,3])       # x =1+2 y=3 x+y=6
print(c)

#封装
# 1.选择排序 选择一个基准球2. 将基准球和余下的球进行一一比较，如果比基准球小，则进行交换3. 第一轮过后获得最小的球　 　
a = [11,5,33,4]
def my(list):
    for i in range(len(list)):
        index = i
        for j in range(index+1,len(list)):
            if list[index]>list[j]:
                list[index],list[j]=list[j],list[index]
    return list

print(my(a))

# 接收用户输入的数字，负数结束，去掉重复数字，字符串输出
def my2():
    list3 = []
    while True:
        some = int(input(";"))
        if some>=0:
            list3.append(some)
        else:
            break
    new = []
    for i in list3:
        if i not in new:
            new.append(str(i))
    ss = ''.join(new)
    return ss
print(my2())