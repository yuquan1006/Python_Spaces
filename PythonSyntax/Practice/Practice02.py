#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/5 17:03
# @Author  : Yuquan
# @Site    :
# @File    : Practice02.py
# @Software: PyCharm

# 1. 我的日程表  变量使用
def course_table():
    yuwen = "语文"
    math = "数学"
    chemistry = "化学"
    tiyu = "体育"

    teacher_y = "陈嗲"
    teacher_m = "张建平"
    teacher_c = "夏嗲"
    teacher_t = "忘记名字了"
    a = '-' * 50
    print("+%s+" % a)
    print("| 1 |            %s |  %s " % (yuwen, teacher_y))
    print("| 1 |            %s |  %s " % (math, teacher_m))
    print("| 1 |            %s |  %s " % (chemistry, teacher_c))
    print("| 1 |            %s |  %s " % (tiyu, teacher_t))
    print("+%s+" % a)
# 2.问问题   输入输出
def askQuestions():
    name = input("你的姓名是？")
    height = input("请输入你的身高？")
    sex = input("请输入你的性别?")
    print("所以你的姓名是：{name}, 性别是：{sex}，身高是：{height}cm".format(name=name, sex=sex,height=height))
# 3.问答
def askQuestions_01():
    name = input("你好。你叫什么名字？ ")
    age = int(input("嗨， %s！你几岁？" % name))
    print("所以你是 %d，是吗？那根本不老！" % age)
    salary = float(input("你每个月的薪水是？"))
    print("8.5！我希望每小时而不是每年！大声笑！")
# 4.五年的年龄
def fiveAge():
    age = int(input("嗨,你几岁？"))

    print("那五年后你的年龄是：%d" % (age+5))
    print("那五年前你的年龄是：%d" % (age-5))
# 5.简单计数器
def add():
    try:
        a = float(input("请输入第一数:"))
        b = float(input("清输入第二个数:"))
        if isinstance(a, float) and isinstance(b, float):
            print(a+b)
        else:
            print("输入错误")
    except:
        print("输入格式不对")
# 6.你几岁  if-elif
def how_age():
    try:
        age = int(input("请输入你的年龄"))
        if isinstance(age,int):
            if  age < 16 and age > 0:
                print("年龄小于16岁，说“你不能开车")
            elif age > 0 and age < 18:
                print("年龄小于16岁，说“你不能开车,年龄小于18岁，说“你不能投票")
            elif age >= 18:
                print("年龄在18岁或以上，说“你可以做任何合法的事情")
            else:
                pass

    except:
        print("输入格式错误")
# 星际体重
def weight():
    try:
        weight = int(input("请输入你在地球的体重（kg）:"))
        print('''我有以下行星的信息：1.金星2.火星3.木星 ''')
        reslut = int(input("你准备去哪个星球"))
        if reslut == 1:
            print("你在金星的体重为:%dkg" %(weight*0.78))
        elif reslut == 2:
            print("你在火星的体重为:%dkg" % (weight * 0.39))
        elif reslut == 3:
            print("你在木星的体重为:%dkg" % (weight * 2.56))
        else:print("暂时未收录该行星的引力")
    except:
        print("输入格式错误！")




# 1.随机数
import random
def randoms():
    print("我的随机数整数是:%s" % random.randint(0, 10))
    print("0-1的随机数浮点数:%s" % random.random())
    print("指定的随机数浮点数:%s" % random.uniform(10, 20))
    print("从指定列表种出随机数:%s" % random.randrange(0, 100, 2))  # 从0-100的偶数种获取随机数
    print("从序列种出随机元素 %s" % random.choice("a bcd"))



if __name__ == '__main__':
    # course_table()
    # askQuestions()
    # askQuestions_01()
    # fiveAge()
    # add()
    # how_age()
    # weight()
    randoms()