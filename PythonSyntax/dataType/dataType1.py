#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# @Version : 1.0  
# @Time    : 2018/4/17  
# @Author  : YUQUAN
# 学习重点：数据结构（列表(list)、元组（Tuple）、字典（Dictionary）和集合（Set

# 列表 是一种用于保存一系列有序项目的集合 列表是一种可变的（Mutable）数据类型，意即，这种类型是可以被改变的
# 可以完成大多数集合类的数据结构实现,它支持字符，数字，字符串甚至可以包含列表（即嵌套
# list = ['china','america','canada','rissia']    # 国家列表
# list[1] = 'NO 1'    # 列表一种可变的（Mutable）数据类型，意即，这种类型是可以被改变的
# list.append('america')    # 列表增加一个项目
# print(list)
# del list[1]   # 删除list第二个元素
# print(list)
# print('国家有：',end='')
# for i in list:
#     print(i,end='')
# print('共有%s个国家\n'%list.__len__())
# list.sort()   # 列表排序


#元祖 用于将多个对象保存到一起。你可以将它们近似地看作列表,但是没有列表类的那么多功能，你不能编辑或更改元组
# hunan = 'chashang','xiangtan','zhuzhou'
# china = ('beijin','shanghai','guangzhou',hunan)
# print(len(china),end='');print(len(hunan))
# print(china[0],china[3][0])
# print(china)


# 字典 字典是无序的对象集合, 你只能使用不可变的对象（如字符串,数字）作为字典的键值,
# phonebook = {
#     'yu':1897309192,
#     'liu':18912345678,
#     'li':18512345678,
#     12:178544554
# }
# print('yu的电话号码是：',phonebook['yu'])   # 通过key来获取value
# del  phonebook['li']              #  删除一对键值对
# phonebook['yuan'] = 18911111111   # 添加一对键值对
# print(phonebook.keys());print(phonebook.values())  # 输入字典的全部键；值
# for name,phone in  phonebook.items():   # phonebook.itmes 来访问字典中的每一对键值—值配对信息，这一操作将返回一份包含元组的列表，每一元组中则包含了每一对相应的信息
#     print('{} 的电话是：{}'.format(name,phone))
# if 'yu' in phonebook:    # in 运算符来检查某对键值—值配对是否存在
#     print(phonebook['yu'])
# print(phonebook[12])

# 序列：列表、元组和字符串可以看作序列（Sequence）的某种表现形式。序列的主要功能是资格测试（也就是 in 与 not in 表达式）和索引操作（既下标）
# 切片
# list = [1,2,3,4,5]
# yuan = (6,7,8,9)
# say ='yuquanaaa'
#
# print('itmes 0 is:',list[0],end='  ');print('itmes 0 is:',yuan[0],end='  ');print('items 0 is:',say[0])
# print(list[1:-1])   # 使用负数下标，位置计数将从队列的末尾开始。
# print(yuan[0:-2])
# print(list[:])    # 返回list列表
# print(list[0:4],end='')
# print(list[1:],end='');print(say[0:6])


# 集合（set）是一个无序不重复元素的序列。
# 基本功能是进行成员关系测试和删除重复元素。
# jihe = {12,'a','b',12}
# jihe2 = set(['c','d',12])
#
# print(jihe)
# print(jihe2)
# print(jihe - jihe2)  # a和b的差集
# print(jihe | jihe2)  # a和b的并集
# print(jihe & jihe2)  # a和b的交集
# print(jihe ^ jihe2)  # a和b中不同时存在的元素
# # 集合测试
# if 'fd' in jihe:
#     print('fd 在集合中')
# else:
#     print('fd没有在集合中')

# 引用 （制作副本）
# shoplist = ['01','02','03']
# copylist = shoplist    # 错误引用 当你创建了一个对象(copy)并将其分配给某个变量(shop)时，变量只会查阅（Refer）某个对象，并且它也不会代表对象本身。只是它们指向的是同一个对象
# copylist = shoplist[:]  # 正确引用  通过生成一份完整的切片制作一份列表的副本。他就是对象本身了


# 字符串更多方法   所有字符串都是str类下的对象
# name = 'yuquan'
# if 'a' in name:            # 检查；a是否在查询的字符串中/一部分
#     print('名字里含有','a')
# if name.startswith('yu'):    # 方法用于查找字符串是否以给定的字符串内容开头
#     print('名字是以','yu','开始的')
# if name.find('qu') != -1:           # 是查找字符串里是否有qu，没有的话返回-1
#     print('名字里含有','qu')
# # 联结 join
# fuhao = '__'
# list = ['中国','美国','俄罗斯']
# print(fuhao.join(list))     # str 类同样还拥有一个简洁的方法用以联结序列中的项目，其中字符串将会作为每一项目之间的分隔符
