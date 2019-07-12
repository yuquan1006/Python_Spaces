#!/usr/bin/python
#author         :YUQUAN
#projectName    :huice_base
#date           :
#version        :PYTHON3.6
#File           :dataType2.py

# 　元祖
a = (2,34,4,7,7)
b = (3,'a','c' )
#1，访问元祖对象 通过索引、切片
# tuple = (x,y)     # 创建
print(a[::-1])      # 倒序输出
# print(a[:])         # 输出全部
# print(a[1:4])        # 切片输出
# print(a[2])         # 索引输出

# 2.元祖元素是不科修改
# a[0] = 5
# print(a)

# 3.元祖拼接+ 、重复* 都是得到一个新的内存地址，既不同的变量a
# print(a+b)
# print(a*4)
# c = '123'
# d =c*3
# print(d[5])

# 4/删除整个元祖
# del a
# print(a)

# 5.内置函数 max、min、len、tuple(将序列转换成元祖）
# print(max(a))
# print(max('b'))
# print(len(a))
# str = '1234jj'
# list = [2,4,'jj',4]
# print(tuple(list))
# print(tuple(str))

# 元素操作 index、count
print(a.index(2))       # 获取元素在元祖中的索引键，默认获取左边第一个
print(a.count(2))       # 获取元素在元祖中出现的次数

# 元祖嵌套
data =((1,'余泉',10000),(2,'余安',12000),(3,'小杨',14000))
# 访问
print(data[1][:])
print(data[1][-1])
# 计算平均工资
# sum = 0
# for i in data:
#     sum += i[-1]
# avg = sum/len(data)
# print(round(avg))
# s输出工资最高的
list =[]
for i in data:
    list.append(i[-1])
list.sort()
print(list[-1])
# s输出工资最高的姓名
# 自己写的
# sal = []
# for i in range(0,len(data)):
#     sal.append(data[i][-1])
# else:
#     for j in range(0,len(sal)):
#         if max(sal) == data[j][-1]:
#             print(j)
#             print(data[j][1])
# 改良版
sal = []
for i in range(0, len(data)):
    sal.append(data[i][-1])
maxsal = max(sal)
print(data[sal.index(maxsal)][-2])
# 通用版（任何语言）
temp = 0
j = 0
# for i in range(len(data)):
#     if data[i][-1]>temp:
#         temp = data[i][-1]
#         j += i
# print(data[j][-2])
# 列表
#１创建
a =[]
a = [2,'44',4,'yu']
list2 = [2,3,9,5,'ii']
# 访问 索引、切片

print(list2[::-1])
# 更新数据项
# 通过索引
a[0] = 200
print(a)
# 批量插入

print('11111111111111111')
a[4:4]=list2         # 从第四项插入一个列表
print(a)
# append 追加
a.append(1212)       # append向列表中加入一个元素
a.append(list2)      # append 加入一个列表时，相当于嵌套了
print(a)

# 删除列表
# del a[2]
# print(a)
# del a
# print(a)

# 列表方法
#append 在列表末尾追加新的元素
a.append('yu')
a.append([1,2,3])
print(a)
#count 统计某元素在列表中出现的次数
print(a.count('yu'))
#reverse 反序输出列表
list2.reverse()
print(list2)

# sort 原地操作函数 原地排序列表(字符按asiic值排） 默认key=none key可以为系统函数也可以为自己建的函数   默认reverse =false 肾虚  reverse =Ture 降序
list4 = ['a','b','cc','ab']
# key = 函数 排序规则为将列表的每一个元素去key等于函数中 如下先按照长度（len）排序，长度一致的话按照降序排
list4.sort(key=len,reverse=True)
print(list4)
list4.sort()
print(list4)
# sorted 新建操作函数
list5 =[3,9009,900,9999]
print(sorted(list5))
# 列子  求工资最高的姓名
data =[[1,'余泉',10000],[2,'余安',12000],[3,'小杨',14000]]
#自己建一个函数 将每一项的【-1】既工资数返回
def mysort(a):
    return a[-1]
# 将列表的每一个元素去key=函数，每次都返回工资，将工资按照降序排
data.sort(key=mysort,reverse=True)
print('```````')
print(data[0][-1])

#第二种 sorted
print(sorted(data,reverse=True,key=lambda x :x[-1]))
print(sorted(data,reverse=True,key=lambda x :x[-1])[0][-1])

#pop 弹出列表中一个元素（删除）
#list2.pop()
# 无参数时，默认从最大索引值删除
list2.pop()
# 参数为索引值，根据索引值弹
list2.pop(0)
print(list2)
#list2.pop(索引值) 返回的是一个索引值对应的元素值     TIP:函数的两种类型；原地操作 如 list.sort list.pop（）新建操作 如str.replace(）list.pop（）
print(list2.pop(0))

# remove 根据元素（值）删除元素
a = [1,2,3,4]
a.remove(2)
print(a)
# index 根据列表元素值找出索引值
list3 = [1,2,34,4]
print(list3.index(4))
# insert 在第四位插入数据‘disige’
list3.insert(4,'disige')
print(list3)

# 将a列表里的偶数位置元素进行+3组成新列表
a =[1,2,3,4,5,6]
new=[x+3 for x in a if x%2 ==0]

a = [1,2,3,4]
b = [5,6,7,8]
new = [x+x1 for x in a if x%2 == 0 for x1 in b if x1%2 == 0]
print(new)

# 运算
# + 两个列表想加，生成一个新列表
a = [1,2,'y']
b = [3,4,'u']
c = a+b
print(c)
# += 效果和extend一样，向列表追加一个新元素
a+=b
print(a)

# 列表嵌套
d = [[1,2,3],[4,5,6],[7,8,9]]
# zip zip函数接受任意多个可迭代对象作为参数,将对象中对应的元素打包成一个tuple,然后返回一个可迭代的zip对象
a = [1,2,3,4]
b = ['y','quan','an']
c = [100,800,900]
zip = zip(a,b,c)
a = []
for i in zip:
    print(i,end='')
    a.append(i)
print(a)



# set集合数据类型 无序不重复元素集
#　创建　set(序列对象） 如元祖、列表
a =set((1,2,3))
print(a)
# 不支持索引和分片
# print(a[0])
# 可以循环
for i in a:
    print(i,end='')

# 操作
# 添加一项
a.add('yu')
print(a)
#删除一项 remove 删除set中元素如元素不存在就报错，discard 删除set中元素如元素不存在也不会报错
a.remove('yu')
print(a)
# 弹出首个元素
a.pop()
print(a)
# 清空
a.clear()
print(a)
# 因为是序列对象，所以可以被转成元祖、列表

# 列表去重
# 方式一 ：循环原始列表，创建新列表
data = [1,25,3,5,2]
new = []
for i in data:
    if i not in new:
        new.append(i)
print(new)
print("111")
# 方式二 用set数据类型对列表去重在转成list数据类型 缺点：会将原来列表里的值排序，破坏数据。
new2 = list(set(data))
print(new2)
# 解决方法 用sorted排序
print(sorted(new2,key = data.index))

# 用字典去重
data = [00,00,7677,777,2]
new5 = {}.fromkeys(data).keys()
print(new5)

# 两个列表合并去重
data = [1,23,33,1,24]
data2 = [23,2,4,33]
# 方式一
new = []
data.extend(data2)
print(data)
for i in data:
    if i not in new:
        new.append(i)
print(new)
#方式二
data3 = data+data2
print(data3)
new = list(set(data3))
print(new)


# 字典 dic = {key:value} 字典是可变数据类型，字典数据是无序的
# key 不可变数据类型（数字、字符串），且重复就会被覆盖  value 可以是任意数据类型
dic = {
        'id' :1,
         'name':'yuquan',
          "sal":8333,
        'sal':10000
      }
print(dic)

#访问数据项
# 通过key  没有索引;不能切片
print(dic.get('id',0))
print(dic['name'])
print(dic.get('sal'))
# 更新数据项 如果key不存在就是新增，存在就是更新
dic['id'] = 2
dic['age'] = 23
dic[5] = 5
print(dic)
# 练习 'k1:1|k2:2|k3:3'将字符串存入字典以这种形式{'k1': '1', 'k2': '2', 'k3': '3'}
str = 'k1:1|k2:2|k3:3'
new = str.split('|')
dic ={}
for i in new:
    key =i.split(":")[0]
    value = i.split(":")[1]
    dic[key] = value
print(dic)
# 删除
del dic['k3']
print(dic)
# del dic
# 字典方法
#要判断一个key是否存在于某个dict中python2可以用has_key,python3后用in 返回Ture。False
str = 'k3'
print(str in dic)
# keys/values 输出字典里所有的键、值。 返回值为iterators，并非直接的列表，若要返回列表值还需调用list函数。
list5 = dic.values()
print(list(dic.keys()))
print(list(list5) )

# 返回一个包含（键，值）元祖的列表。返回值为iterators，并非直接的列表，若要返回列表值还需调用list函数。
print(list(dic.items()))

# pop（key）1.删除key项 2.返回对应key包含的value值
print(dic.pop('k2'))
print(dic)
# clear 清楚字典里所有的项或元素
dic.clear()
print(dic)
# copy 返回一个字典拷贝的副本
dic = {'sam':'1234','tom':'5678'}
dic2 = dic.copy()
print(dic2)

#字典初始化 创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值。
dictt ={}
p = ['zhangsna','lisi','yuwu']
dictt = dictt.fromkeys(p,90)
print(dictt)
# 合并列表  字典更新，将字典d2的键值添加到字典d1去，如果key存在，就更新value值，key不存在就新增
d1 = {'k1':1}
d2 = {'k2':2}
d1.update(d2)
print(d1)

# 运算
# 字典里没有拼接和重复操作符 + 、* 运算
# print(d1 + d2)

# 迭代
dic = {'name':'yuquan','id':1,'sal':20000}
#便利字典里的key
for i in dic.keys():
    print(i)
#便利字典里的value
for i in dic.values():
    print(i)
#遍历字典里的项
for i in dic.items():
    print(i)
# 便利字典里的key和value
for i,j in dic.items():
    print(i,j)

# 练习 去除字典中value重复的的项
dic ={'sam':78,'tom':61,'li':78}
# 字典在迭代是不可以改变大小，建议转成列表或集合
for i,j in list(dic.items()):
    value = list(dic.values())
    if value.count(j)>1:
        del dic[i]
print(dic)

#sort
# 对字典的Value排序           按照最后一个元素生序排列
print(sorted(dic.items(),key=lambda x :x[-1],reverse=True)
)

#练习
data = {
        'yuquan': 99,
        'yuan': 67,
        'lisi':77,
        'zhangsan': 68
}
# 算出平均分
# 方式一
# sum = 0
# count = 0
# for i in list(data.values()):
#     sum = sum+i
#     count +=1
# print(sum/count)
#方式二
list_data = list(data.values())
def avg(a):
    return sum(a)/len(a)
print(avg(list_data))
# 2.找出学霸
# 方法一
# temp = 0
# for i,j in list(data.items()):
#     if j>temp:
#         temp = j
#         print(data[i])
#方法二
print(sorted(data.items(),key=lambda x :x[-1],reverse=True)[0][0])

#练习二
data = {
        'yuquan': [99,100,89],
        'yuan': [67,18,69],
        'lisi':[44,34,67],
        'zhangsan':[98,56,99],
}
# 找出平均分不足60的人
for i,j in data.items():
    if sum(j)/len(j) < 60:
        print('平均分不足60的人是：%s%s' % (i, i))
#找出各科最高分
list1 = []
list2 = []
list3= []
for j in data.values():
    list1.append(j[0])
    list2.append(j[1])
    list3.append(j[2])
a = sorted(list1)[-1]
b = sorted(list2)[-1]
c = sorted(list3)[-1]
print('语文最高分是：%s'%a)
print('数学最高分是：%s'%b)
print('英语最高分是：%s'%c)
#算出各科平均分，在找出学霸
for y in data.keys():
    if a == data[y][0]:
        print(y)
    if b == data[y][1]:
        print(y)
    if c == data[y][2]:
        print(y)

print(sum(list1)/len(list1))
print(sum(list2)/len(list1))
print(sum(list3)/len(list1))

# 练习
data = {
        '余泉':{'语文':78,'数学':100,'英语':89},
        '余安':{'语文':97,'数学':99,'英语':66},
        '余世星':{'语文':32,'数学':10,'英语':49},
        '余玲':{'语文':48,'数学':50,'英语':44}
        }
# 找出平均分不足60分的人
def avg(list):
    return sum(list)//len(list)

list = []
for i,j in data.items():
    for l in j.values():
        list.append(l)
    if avg(list) < 60:
        print(i)
    list.clear()

# 找出各科最高分，平均分
yuwen =[]
shuxue=[]
yingyu=[]
list =[]
for k,i in data.items():
    for j in i.values():
        list.append(j)
    yuwen.append(list[0])
    shuxue.append(list[1])
    yingyu.append(list[2])
    list.clear()
print(max(yuwen),avg(yuwen))
print(max(shuxue),avg(shuxue))
print(max(yingyu),avg(yingyu))

# 第二种解法
yuwen = {}
shuxue = {}
yingyu = {}
score_list = []

for name, score_dic in data.items():
    score_list = score_dic.values()
    yuwen[name] = score_dic.get("语文")
    shuxue[name] = score_dic.get("数学")
    yingyu[name] = score_dic.get("英语")
    if avg(score_list) < 60:
        list.append(name)
# 找出各科最高分，平均分和学霸
print("品均分不足60的人：",' '.join(list))
print("语文最高分是：%s 数学最高分是：%s 英语最高分是： %s"%(max(yuwen.values()),max(shuxue.values()),max(yingyu.values())))
print("语文平均分是：%s 数学平均分是：%s 英语平均是： %s"%(avg(yuwen.values()),avg(shuxue.values()),avg(yingyu.values())))
print("语文学霸是：%s 数学学霸是：%s 英语学霸是： %s"%(max(yuwen,key=yuwen.get),max(shuxue,key=shuxue.get),max(yingyu,key=yingyu.get)))
print("语文学霸是：",sorted(yuwen.items(),key=lambda x:x[-1],reverse=True)[0][0])