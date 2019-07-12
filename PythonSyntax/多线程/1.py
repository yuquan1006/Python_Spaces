#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 13:21
# @Author  : Yuquan
# @Site    : 
# @File    : 1.py
# @Software: PyCharm
import time
import threading
#
# #
# def start_game():
#     print("开始打lol游戏 %s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
#     time.sleep(1)
#     print("开始打DNF游戏 %s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
#     time.sleep(1)
#     print("游戏完成！%s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
#
# def start_stu():
#     print("开始学习PYTHON %s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
#     time.sleep(1)
#     print("开始学习JAVA %s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
#     time.sleep(1)
#     print("学习完成！%s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
#
# # # 单线程运行 ： 一个一个执行
# # start_game()
# # start_stu()
#
# # # 多线程执行：一起运行
# #
# # 创建线程数组
# threads = []
# # 创建线程t1，并添加到线程数组
# t1 = threading.Thread(target=start_game)
# threads.append(t1)
#
# # 创建线程t2，并添加到线程数组
# t2 = threading.Thread(target=start_stu)
# threads.append(t2)
#
# if __name__ == '__main__':
#     # 启动线程
#     for i in threads:
#         i.start()



# 2.带参数的用args传元组类型（参数最后多加一个逗号“,”要不然会报错） ,或者用kwargs传字典{}类型
# def start_game(threadName):
#     print("%s 线程开始！" % threadName)
#     print("开始打lol游戏 %s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
#     time.sleep(1)
#     print("开始打DNF游戏 %s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
#     time.sleep(1)
#     print("游戏完成！%s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
#
# def start_stu(threadName):
#     print("%s 线程开始！" % threadName)
#     print("开始学习PYTHON %s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
#     time.sleep(1)
#     print("开始学习JAVA %s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
#     time.sleep(1)
#     print("学习完成！%s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
#
# threads = []
# t1 = threading.Thread(target=start_game, args=("游戏",))
# threads.append(t1)
# t2 = threading.Thread(target=start_stu, kwargs={"threadName":"学习"})
# threads.append(t2)
#
# if __name__ == '__main__':
#     for i in threads:
#         i.start()



# 3 定义自己的mythrea类，重写run方法
# 备注：这里运行结果会有个问题，主线程已经退出了，子线程Thread-1和Thread-2还在跑。这就是后面需要讲的守护线程了。。。
'''1.start()方法 开始线程活动。
对每一个线程对象来说它只能被调用一次，它安排对象在一个另外的单独线程中调用run()方法（而非当前所处线程）。
当该方法在同一个线程对象中被调用超过一次时，会引入RuntimeError(运行时错误)。
2.run()方法 代表了线程活动的方法。
你可以在子类中重写此方法。标准run()方法调用了传递给对象的构造函数的可调对象作为目标参数，如果有这样的参数的话，顺序和关键字参数分别从args和kargs取得'''


# 场景一：主线程已经结束了，子线程还在跑
def start_stu(people):
    print("%s 学习Java %s" %(people,time.ctime()))
    time.sleep(1)
    print("%s 学习Python %s" %(people,time.ctime()))
    time.sleep(1)
    print("%s 学完了！%s"%(people,time.ctime()))


class MyThread(threading.Thread):
    def __init__(self, threadName, people):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.people = people

    def run(self):
        print("开始线程 %s" % self.threadName)
        start_stu(self.people)
        print("结束线程")

t1 = MyThread("Thread-1", '余泉')
t2 = MyThread("Thread-2", '余安')
t1.start()
t2.start()
time.sleep(1)
print('退出主线程 教室关灯走人')  # 1.我们把t1.start()和t2.start()称为两个子线程，写在外面的代码就是主线程了。






# 场景二 主线程结束，子线程必须结束
'''1.主线程中，创建了子线程t1和t2，并且在主线程中调用了thread.setDaemon(),这个的意思是，把主线程设置为守护线程，这时候，要是主线程执行结束了，就不管子线程是否完成,一并和主线程退出.'''
# def start_stu(people):
#     print("%s 学习Java %s" %(people,time.ctime()))
#     time.sleep(1)
#     print("%s 学习Python %s" %(people,time.ctime()))
#     time.sleep(1)
#     print("%s 学完了！%s"%(people,time.ctime()))
#
#
# class MyThread(threading.Thread):
#     def __init__(self, threadName, people):
#         threading.Thread.__init__(self)
#         self.threadName = threadName
#         self.people = people
#
#     def run(self):
#         print("开始线程 %s" % self.threadName)
#         start_stu(self.people)
#         print("结束线程")
#
# t1 = MyThread("Thread-1", '余泉')
# t2 = MyThread("Thread-2", '余安')
#
# # 守护主线程
# t1.setDaemon(True)
# t2.setDaemon(True)
#
# t1.start()
# t2.start()
# time.sleep(1)
# print('退出主线程 教室关灯走人')  # 1.我们把t1.start()和t2.start()称为两个子线程，写在外面的代码就是主线程了。




# 场景三：主线程等待子线程结束后再运行，就需要用到join(),此方法是在start之后（与setDaemon相反），join(timeout)此方法有个timeout参数，是线程超时时间设置。

# def start_stu(people):
#     print("%s 学习Java %s" %(people,time.ctime()))
#     time.sleep(1)
#     print("%s 学习Python %s" %(people,time.ctime()))
#     time.sleep(1)
#     print("%s 学完了！%s"%(people,time.ctime()))
#
#
# class MyThread(threading.Thread):
#     def __init__(self, threadName, people):
#         threading.Thread.__init__(self)
#         self.threadName = threadName
#         self.people = people
#
#     def run(self):
#         print("开始线程 %s" % self.threadName)
#         start_stu(self.people)
#         print("结束线程")
#
# t1 = MyThread("Thread-1", '余泉')
# t2 = MyThread("Thread-2", '余安')
#
# t1.start()
# t2.start()
#
# # 阻塞主线程，等子线程结束
# t1.join(timeout=10)
# t2.join(timeout=10)
#
# time.sleep(1)
# print('退出主线程 教室关灯走人')  # 1.我们把t1.start()和t2.start()称为两个子线程，写在外面的代码就是主线程了。
