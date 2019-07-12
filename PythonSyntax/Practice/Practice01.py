#!/usr/bin/python
#author         :YUQUAN
#projectName    :huice_base
#date           :
#version        :PYTHON3.6
#File           :Practice01.py

# chr（） 函数  将整数转化成对应assic字符
# some = int(input("请输入数字"))
# if chr(some):
#     print(chr(some))
# print(67+32)
#
# # ord（） 函数  将assic字符转化成对应整数
# while True:
#     some = input("请输入A-Z:")
#     change = ord(some)
#     if 65<= change <=120:
#         print("你输入的字母对应的Assic值：",change)
#         break
#     else:
#         print("你输入的字符有误")

# a = '''yuquan
#         NO 1
#     '''
# b = 'yuquan \n no1'
# c = 'bad say  i\'m ok'
# d = 'div[@good=\'yes\']/a'
# print(c)


#　奇偶数
# some = int(input("请输入数字："))
# somes = str(some)
# if some % 2 == 0 :
#     print('你输入的数%s,是偶数'%(some))
#     print(somes[:])
# else:
#     print("你输入的数%s,是奇数"%(some))

# format 函数
# pp = 'http'
# url = "wwww.baidu.com"
# data = 'key=value'
# # address = '{0}://{1}?{2}'.format(protocol,url,data)
# address = "{procotol}://{url}?{data}"
# print(address.format(procotol=pp,url=url,data=data))

# 拼接动态函数
# def test_casexx:
#     '测试用例描述'
#     execute_case(data)     # 这个函数中用例标号、用例描述、参数都为变量 如何拼接这个动态函数？

# abc = '''def {test_case}(self):
#     '{defind}'
#     execute_case({data})
# '''
# print(abc.format(test_case='test_case01',defind='测试用例描述',data='id=1'))


# 字符串去空格
# str.strip()     去除字符串左右两边空格
# str.lstrip()       去除字符串左边空格
# str.rstrip()        去除字符串右边空格
# a = '890 '
# a = a.strip()
# print(len(a))
# if a == '890':
#     print("价格相等")
# else:
#     print("价格不相等")

# 其他
# str.isalnum()
# str.isalpha()
# str.isdigit()
# str.isspace()
# str.count(target,[min,max]) #统计某个字符在字符串中出现的次数
# str.startswith(target)      #判断某个字符串是否以某个字符串开始
# str.endswith(target)        #判断某个字符串是否以某个字符串结束

# str.capitalize()：只保留str中首字母大写  返回一个只有首字母大写的字符串
# str.lower()：将str中的大写字母转小写字母
# str.upper()：将str中的小写字母转成大写字母
# str = 'yu fdsifsdkl dfjidiusiofiosd fdisofio soif ' # 这个字符串含有空格哦
# #统计某个字符在字符串中出现的次数
# print(str.count('f'))
# #判断某个字符串是否以某个字符串开始
# if str.startswith('y'):
#     print('yes')
# # 判断是否全是空白字符，并至少有一个字符
# print(str.isspace())
# # 判断是否全是数字，并至少有一个字符
# print(str.isdigit())
# str = 'yuquanaaaaaaaaaaaaaa'
# # 判断是否全是字母，并至少有一个字符
# print(str.isalpha())
# #判断是否全是字
# 母和数字，并至少有一个字符
# print(str.isalnum())

#给定一个字符串找出第一个不重复的字符输出他是第几位 ?'
# print('111111111111111111111111111111111111111111111111111111')
# target = 'hello yuquan'
# for x in target :
#     if target.count(x) == 1:
#         print(x)
#         print('他是%s 位'%target.index(x))
#         break

# 去除上一题中的重复字符，得到一个新的字符串
# list = []
# for i in target:
#     if i not in list:
#         list.append(i)
# str = ''.join(list)
# print(str)

# 接收用户输入的数字，负数结束，去掉重复数字，字符串输出
# list3 = []
# while True:
#     some = int(input(";"))
#     if some>=0:
#         list3.append(some)
#     else:
#         break
# new = []
# for i in list3:
#     if str(i) not in new:
#         new.append(str(i))
# str = ''.join(new)
# print(str)
# 输出一个模拟风车等待图标
# while True:
#     tibiao = ['|', '/', '-', '\\']
#     for x in tibiao:
#         print(x+'\r', end='')              # \r代表的是最左边打印x的值,并且不换行




# 输入一个字符串，判断是否为纯数字
# some = input('请输入：')
# print(some)
# if some.isdigit():
#     print('yes')
# else:
#     print('no')

# if 两个表达形式：1、if 条件表达式（0 >= 0）：  2简写 if x：x为下面1的时候，条件不成立
# 1.None、0、空字符串、空元祖、空列表、空字典判断为false 不执行if下代码块
a = ''
if a:
    print('存在')
# python无switch语句，所以多个条件时可以用elif语句来实现
# score = int(input('输入你的学习成绩'))
# if 80<score<=100:
#     print('你的成绩为%s，为优秀'%score)
# elif 60<=score<=80:
#     print('你的成绩%s，为中等')
# elif score<60:
#     print('你的成绩低等')
# else:
#     print('你输入成绩有误')

#　输入一个正整数，判断是否可以被２和７整除
# num = (input('请输入：'))
# if num.isdigit():
#     int_num = int(num)
#     if int_num%3 and int_num%7:
#         print('%d可以被3和7整除' %int_num)
#     else:
#         print("no")
# # else:
#     print('%s不是正帧数' %num)

# 根据输入月份来输出天数（二月默认28）
# while 1:
#     month = input('请输入月份：')
#     if month.isdigit():
#         int_month = int(month)
#         if int_month in range(1,13):
#             if int_month in(1,3,5,7,8,10,12):
#                 print('%d月有31天'%int_month)
#                 break
#             elif int_month==2:
#                 print('%d月有28天'%int_month)
#                 break
#             else:
#                 print('%d月有30天'%int_month)
#                 break
#         else:
#             print('你输入的月份非1-12，请重新输入：')
#     else:
#         print('你输入月份信息为非数字！请重新输入：')

# 输入年份，判断是否是润年
# some = input('请输入年份：')
# if some.isdigit():
#     int_year = int(some)
#     if int_year%4 == 0 and int_year%100 != 0 or int_year%400 == 0:
#         print('%d是闰年'%int_year)
#     else:
#         print('{year}不是闰年'.format(year=int_year))

# 输入通话时间，得出话费
# time = input('输入通话时间')
# money = 0
# if time.isdigit():
#     int_time = int(time)
#     if int_time<=180:
#         money = 0.2
#         print(money)
#     else:
#         if (int_time-180)%60 ==0:
#             money = (int_time-180)/60*0.1+0.2
#             print(round(money,1))
#         else:
#             money=0.2+((int_time-180)/60+1)*0.1
#             print(round(money,1))

# for
# 1.循环序列（字符串、元祖、列表）
# num = [0,1,2,3,4,5]
# for x in num:
#     print(x)

# 2.循环rangge函数和xrangge函数


# 练习
#1.输入n，计算1到n的阶乘
# n=4 阶乘 = 1*2*3*4
# n = input('请输入：')
# sum = 1
# total = 0
# int_n = int(n)
# for x in range(1,int_n+1):
#     sum=sum*x
# print(sum)

# 循环输出1-100的偶数
# for x in range(1,101):
#     if x % 2 == 0:
#         print(x)

# for x in range(0,101,2):
#     print(x)

# 找100以内最大平方数
# # 取整数 1.拿该数去对1求余如果值为0，该数就是整数
#         2.拿该数去和int(该数)的值比较如果相等，该数就是整数
# print(9.0 == int(9.0))
# print(9.123 == int(9.0))
# from math import sqrt
# for x in range(101,0,-1):       # range的倒着取值
#     if sqrt(x) % 1 == 0:
#         print(x)
#         break #continue     # break 和 continue的区别

#输入字符串，计算他有多少个字符，数字，空格，其他。
# some = input('请输入字符串：')
# digit = 0
# alpha = 0
# space = 0
# other = 0
# for x in some:
#     if x.isdigit():
#          digit += 1
#     elif x.isalpha():
#         alpha += 1
#     elif x.isspace():
#         space += 1
#     else:
#        other += 1
# print('你输入的字符串，字符共有%d个，数字共有%d个，空格共有%s个，其他共有%s个'%(alpha,digit,space,other))


# 输入一个整数，判断是否是回文数  回文数既：12321 个位与万位相等，十位与千位相等
# some = input('请输入：')
# if some.isdigit():
#     for x in range(len(some)):
#         if some[x] != some[-x-1]:
#             print('no 回文数')
#             break
#     else:
#         print('is 回文数')
# else:
#     print('你输入不是 整数')


#水仙花数（100-999） 例 153  1**3+5**3+3**3=153  一个三位数的每个位的三次方想加等于该数
# 输出三位数中所有水仙花数
# for i in range(1,10):
#     for j in range(0,10):
#         for k in  range(0,10):
#             num = '%d%d%d'%(i,j,k)
#             if i**3+j**3+k**3 == int(num):
#                 print('%s 不是水仙花数'%num)
#             else:
#                 continue
#                 print('%s 是水仙花数'%num)
# # 输出三位数最大的一个水仙花数
# for a in range(999,101,-1):
#     baiwei = a//100             # //是橡皮除，去掉小数点后数
#     shiwei = a//10-baiwei*10
#     gewei = a%10
#     if baiwei**3 + gewei**3 + shiwei**3 == a:
#         print(a)
#         break
#

# for c in range(100,1000):
#     baiwei = int(str(c)[0])
#     shiwei = int(str(c)[1])
#     gewei = int(str(c)[2])
#     if c == baiwei ** 3 + gewei ** 3 + shiwei ** 3 :
#         print(c)

# 输出 99乘法表
# for i in range(1,10):
# # #     for j in range(1,i+1):
# # #         print('%d * %d = '%(i,j),i*j,end='    ')
# # #     print('')

# 100之内的素数
# conut = 0
# for i in range(1,100):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         print('wanshu',i)
#         conut += 1
# print(conut)

# 冒泡排序 原理：每轮只能将一个数归位，如果有n的个数，就要将n-1个数归位
# list = [1,40,20,30]
# for i in range(len(list)-1):            # 确定循环的轮数，比如四个数就要三轮，每轮确定一个最大数。
#     for j in range(len(list)-i-1):      # 每轮循环需要比较的次数 比如 list = [1,40,20,30] 需要比较3次
#         if list[j] >list[j+1]:
#             list[j],list[j+1] = list[j+1],list[j]
# print(list)

# 选择排序
# 1. 选择一个基准球2. 将基准球和余下的球进行一一比较，如果比基准球小，则进行交换3. 第一轮过后获得最小的球　　
# list = [60,30,20,40]
# # for i in range(len(list)-1):            # 确定循环的轮数，比如四个数就要三轮，每轮确定一个最小数。
# #     index = i                           # 从0比较n-1 index为基准球位置下标
# #     for j in range(i+1,len(list)):      #　用index的值分别与后面的值进行比较,以便获取最小index
# #         if list[index]>list[j]:         #　如果找到比当前值小的index,则进行两值交换
# #             list[index],list[j] = list[j],list[index]
# #
# # print(list)

#　出租车计费　输入距离和等待时间 三公里10元 超过三公里的没0.5加收一元，没等待2.5分钟加收一元 超过15公里加收原价的%5o
# 输入km和s
# some = input(':')
# list = some.split(' ')
# wait = int(list[1])
# long = int(list[0])
# money = 0
# if long<3:
#     money = 10
# elif 3<long<15:
#     money = 10+int((long-3)/0.5)
# elif long>15:
#     money = (10+int((long-3)/0.5))*1.5
# if wait>150:
#     money += wait / 150
# print(money)

# 完数 如果一个数恰好等于它的因子之和，则称该数为完数
# for x in range(2,1001):
#     list = []
#     for i in range(1,x):
#         if x % i == 0:
#             list.append(i)
#     if x == sum(list):
#         print(x)



# 面试题：如何统计数组中出现次数最多的数据，按出现次数由大到小排序
# a = ["a", "b", "a", "c", "a", "c", "b", "d", "e", "c", "a", "c"]
#
# new = list(set(a)) #去重
# dict = {}
# for i in new:
#     c = a.count(i)
#     dict[i] = c    # 次数和值存入字典
# print(dict)
#
# new_dict = sorted(dict.items(), key=lambda x:x[-1],reverse=True) # 按次数排序
# print(new_dict)
# new_list = []
# for i in new_dict:
#     new_list.append(i[0])       # 转化城列表
# print(new_list)

# zip
a = ['余泉', '余安']
for i in zip(range(10),a):
    print(i)
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c", "d", "e"]
# 如何得出c = ["a1", "b2", "c3", "d4", "e5"]
c = [str(y)+str(x) for x,y in zip(a,b)]
print(c)

# 统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]

a = [1, 3, 5, 7, 0, -1, -9, "r", -5, 8]
def calc(a):
    fu = []
    zen = []
    zero = []
    for i in a:
        try:
            if i < 0:
                fu.append(i)
            elif i == 0:
                zero.append(i)
            else:
                zen.append(i)
        except:
            print('该队列存非数字')
    print("%s中负数有%s个，整数%s个，为0的有%s" %(str(a),str(len(fu)),str(len(zen)),str(len(zero))))
calc(a)

# 字符串 "axbyczdj"，如果得到结果“abcd”
s = "axbyczdj"
new = ''.join([b for a,b in enumerate(s) if a%2==0])
print(new)

s = "axbyczdj"
new = s[::2]
print(new)

# 已知一个字符串为“hello_world_yoyo”, 如何得到一个队列 ["hello","world","yoyo"]
s = "hello_world_yoyo"
new = s.split("_")
print(new)

# 已知一个数字为1，如何输出“0001”
i = 1
print("%04d"%i)

# 打印出100-999所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
for i in range(100,999):
    g = i%10
    s = i//10%10
    b = i//100
    if g**3+s**3+b**3 == i:
        print(i)

# 如果一个数恰好等于它的因子之和，则称该数为“完全数”，又称完美数或完备数。 例如：第一个完全数是6，它有约数1、2、3、6，除去它本身6外，其余3个数相加，
# 1+2+3=6。第二个完全数是28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。
# 那么问题来了，求1000以内的完全数有哪些？


for i in range(1000):
    temp = []
    for j in range(1,i):
        if i%j==0:
            temp.append(j)
    if i==sum(temp):
        print(i)

# 用python写个冒泡排序
a = [22,2,33,12]
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]

print(a)
# 用python写个选择排序
a = [22,2,33,12]
for i in range(len(a)-1):
    small = i
    for j in range(i+1,len(a)):
        if a[small]>a[j]:
            a[small],a[j] = a[j],a[small]

print(a)

# 计算n!,例如n=3(计算321=6)， 求10!
def fn(n):
    sum = 1
    for i in range(1, n+1):
        sum = sum * i
    print(sum)
fn(4)

def fn_01(n):
    if n == 1:
        return 1
    else:
        return fn_01(n - 1) * n
print(fn_01(5))

# 斐波那契数列 已知一个数列：1、1、2、3、5、8、13、。。。。的规律为从3开始的每一项都等于其前两项的和，这是斐波那契数列。求满足规律的100以内的所以数据
def fb(n=100):
    a = 1
    b = 1
    list = [1]
    while b<=n:
        list.append(b)
        a ,b =b,a+b

    print(list)
fb()







import re
a = re.search(r'a', "abcderf")  # 查找
print(a.group())
b = re.match(r'b', "abcdef")    # 匹配  严格匹配不行就返回空
print(b)

a = (1,)    # 元祖
b = (1)  # 非元祖
print(type(a))
print(type(b))
import time
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
print(now)
import datetime
print(datetime.datetime.now()-datetime.timedelta(hours=1))