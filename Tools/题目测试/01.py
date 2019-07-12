#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 17:14
# @Author  : Yuquan
# @Site    : 
# @File    : 01.py
# @Software: PyCharm
# 根据题库内容出单选题
# 2.提示做答，并给出结果

import json,os,sys
def main():
    filename = 'question_library.json'
    question_library =read_question_file(filename)
    if not question_library:
        print('题库文件读取失败，请检查{0}'.format(filename))
        sys.exit(-1)
    question_list = question_library['questions']
    question_name = question_library['name']
    print('欢迎来到测验！当前题库为:{0}'.format(question_name))
    input("输入任意键进入")
    count = 0
    for num,i in enumerate(question_list):
        num += 1
        if ask_question(i,num):
            count += 1
    total = len(question_list)
    success = count
    print('测验完成!,您一共完成%s个问题，其中答对%s个，错误%s个'%(str(total),str(success),str(total-success)))


def ask_question(question,num):
    '''打印题目内容和选项，返回题目测试结果'''
    print("\n第{0}题.{1}".format(num,question["question"]))
    for i in range(len(question['options'])):
        print("{0}.{1}".format(to_letter(i),question['options'][i]))
    user_input = input('思考后，请输入你的答案:')
    user_answer,ok = to_answer(user_input)
    while not ok:
        user_input = input('输入错误！请输入选项前单个字母作为答案:')
        user_answer, ok = to_answer(user_input)
    return user_answer == question['answer']


def to_answer(letter):
    '''检查用户输入是否合法，合法就转化对应数字'''
    options_list = ["A","B","C","D"]
    letter = letter.upper()

    if len(letter) == 1 and letter in options_list:
        digit = ord(letter)-ord('A')
        return digit,True
    else:
        return None,False


def read_question_file(filename):
    '''读取题库json文件'''
    if not os.path.isfile(filename):
           return None
    with open(filename,'rb') as f:
        try:
            return json.load(f) #load() 读取json信息
        except BaseException as e:
            print(e)
            print('加载题库错误.')
            return None



def to_letter(n):
    '''把数字0-4转化城对应的A-D'''
    return chr(ord('A')+n)
if __name__ == '__main__':
    main()