#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/5 18:50
# @Author  : Yuquan
# @Site    : 
# @File    : dataType2.py
# @Software: PyCharm
from selenium import webdriver
import time
# 学习点：常见的八种元素定位

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
# driver.get("http://www.moiiee.com")

# 1 find_element_by_id() 通过id属性值来查找元素,.定位到搜索框后，用 send_keys()方法, 输入文本
# driver.find_element_by_id("kw").send_keys("python+selenium")
# time.sleep(1)

# 2 find_element_by_name() 通过name属性值来查找元素,定位到搜索框后，用clear() 清空输入框文本
# driver.find_element_by_name("wd").clear()
# time.sleep(1)

# 3 find_element_by_class_name() 通过class属性值来查找元素
# driver.find_element_by_class_name("s_ipt").send_keys("class_name")
# 页面class 属性多个 class=“clas1 clas2”，取其中一个就行
# driver.find_element_by_class_name("clas1").send_keys("class_name")
# time.sleep(1)

# 4 find_element_by_tag_name() 通过标签属性来查找元素   一个页面相同便签名肯定很多，故一般不用该方法定位
# driver.find_element_by_tag_name("input").clear()

# 5 find_element_by_link_text() 通过文本值来查找元素 一般用于有超链接的元素
# driver.find_element_by_link_text("hao123").click()
# 如果文本很长可以使用模糊匹配 find_element_by_partial_link_text（）
# driver.find_element_by_partial_link_text("123").click()
# time.sleep(2)







# 6 xpath 路径语言
# 6.1 xpath 通过元素属性(id,class,name)定位
# driver.find_element_by_xpath("//*[@id='kw']").send_keys('xpath_01')
# driver.find_element_by_xpath("//*[@id='kw']").send_keys('11')
# 多个class可以取全部
# driver.find_element_by_xpath("//*[@class='class1 class2']").send_keys('xpath_01')

# 6.2 通过其他属性定位元素
# driver.find_element_by_xpath("//*input[@autocomplete='off']").clear()

# 6.3 通过便签+属性定位元素  属性同名的情况下可以用便签+属性。不用便签就要* 表示任意标签
# driver.find_element_by_xpath("//input[@maxlength='255']").send_keys('555')

# 6.4 通过层级定位元素
# driver.find_element_by_xpath("//div[@id='u1']/a[@name='tj_trvideo']").click()  # 父级
# driver.find_element_by_xpath("//div[@class='head_wrappe']/div[@id='u1]/a[@name='tj_trvideo']")


# 6.5 通过索引定位元素(父元素相同)  在一个元素它的兄弟元素跟它的标签一样下使用  下标从1开始
# driver.find_element_by_xpath(".//*[@id='u1']/a[1]").click()
# driver.find_element_by_xpath(".//*[@id='u1']/a[4]").click()

# 6.5.2 多个相同元素但父元素不相同  处理：定位这一组元素，取下标（从0开始）
driver.find_elements_by_xpath("//a[@class='mnav']")[0].click()


# 6.6 逻辑运算 and,or,not  常用 and
# driver.find_element_by_xpath("//input[@id='kw' and @name='wd']").send_keys('6666')

# 6.7 模糊匹配
# 1.模糊匹配文本  重要
# driver.find_element_by_xpath("//a[contains(text(),'hao123')]").click()  # text()函数表示获取文本

# 模糊匹配某个属性值
# driver.find_element_by_xpath("//a[contains(@name,'tj_trhao123')]").click()
# 模糊匹配属性值以什么开始
# driver.find_element_by_xpath("//a[starts-with(@name,'tj_trha')]").click()
# 模糊匹配属性值以什么结束  有问题
# driver.find_element_by_xpath("//input[ends-with(@id,'w')]").send_keys('4545')
# 正则表达式
# driver.find_element_by_xpath("//*[matchs(text(),'hao123')]").click()
# driver.find_element_by_xpath(".//*[@id='app']/div/header/div[1]/section/ul/li[1]/span").click()

# 6.8 文本属性 比如<a class="mnav" name="tj_trmap" href="http://map.baidu.com">地图</a>
# driver.find_element_by_xpath("//a[text()='地图']")
# driver.find_element_by_xpath("//a[text()='新闻']").click()

# 6.9 .. 两点表示上一层 通过定位子元素找父元素
# driver.find_elements_by_xpath("//a[@class='mnav']/..")

# 6.10 firepath调试/浏览器调试：F12之后，点开console 输入格式：$x(“xpath语法”)  然后回车。可以用click，val（输入）




# 7 css
# 7.1 元素属性定位
# driver.find_element_by_css_selector("#kw").send_keys('TTTT') # id属性值
# driver.find_element_by_css_selector(".s_ipt").send_keys('TTTT') # class属性值
# # 页面class 属性多个 class=“clas1 clas2”
# driver.find_element_by_css_selector(".clas1.clas2").send_keys('TTTT') # class属性值

# 7.2 便签名
# driver.find_element_by_css_selector("input").send_keys('TTTT') # 便签名
# 7.3其他属性
# driver.find_element_by_css_selector("[name='wd']").send_keys('TTTT') # name属性值
# 7.4 标签+属性
# driver.find_element_by_css_selector("input[name='wd']")
# driver.find_element_by_css_selector("input#kw").send_keys('TTTT')
# driver.find_element_by_css_selector("input:contains('kw')").send_keys('TTTT')

# 7.5 层级关系
# driver.find_element_by_css_selector("form#form>span.iptfocus>input").send_keys('TTTT')

# 7.6 索引 从一开始
# driver.find_element_by_css_selector(".setpref").click()
# driver.find_element_by_css_selector("select#nr>option:nth-child(1)").click()

#逻辑运算
# driver.find_element_by_css_selector("input[class='s_ipt'][id='kw']").send_keys('TTTT')
# driver.find_element_by_css_selector("input.s_ipt[id='kw']").send_keys('TTTT')

#

# 页面隐藏元素定位？
# selenium可以定位，但是点击报错，用js/jquery去点击

# 页面跳转时，最好sleep等待加载完成
time.sleep(1)
driver.quit()

# 元素不唯一怎么办？
# 1.定位一组元素取下标
# driver.find_elements_by_class_name(“xx”)[1]

# class属性有空格？
# class属性有空格是多重属性，取其中一个就行

# BY定位元素 (八种定位都可以用find_element+By实现)
# from selenium.webdriver.common.by import By
# driver.find_element(By.CSS_SELECTOR, "#KW")
driver.maximize_window()