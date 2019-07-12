#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6

import unittest

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 15:09
# @Author  : Yuquan
# @Site    :
# @File    : demo.py
# @Software: PyCharm
'''
unittest 只有三种结果
1.出现E 表示自己写的代码语法错误
2.出现F 测试用例不通过
3.出现. 测试通过

'''
import unittest,requests

class WeatherTest(unittest.TestCase):
    '''
    测试天气接口
    '''


    def setUp(self):

        self.s = requests.session()
        self.url = "http://v.juhe.cn/weather/index"
        self.headers= {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
        }
    def tearDown(self):
        self.s.close()

    def testAdd01(self):
        '''
        用例描述：cityname 传入上海
        期望结果：reason 返回 successed or
        '''
        params = {
            "cityname": "上海",
            "key": "80b4d4e1d870d257d3344fcf2d08f64a"
        }
        r = self.s.get(self.url, params=params, headers=self.headers)
        print(r.json())
        # 万能断言 参数为真 断言通过
        self.assertTrue(r.json()['reason'] == "successed!" or r.json()['reason'] == "查询成功")
        a = 10
        b = 20
        c = [44,55,66]
        self.assertTrue(a != b)
        # self.assertTrue(a not in b)
        # self.assertTrue(a in b)
        self.assertTrue(len(c))
        result = "{'resultcode': '200', 'reason': 'successed!', 'result': {'sk': {'temp': '15', 'wind_direction': '北风', 'wind_strength': '0级', 'humidity': '35%', 'time': '21:00'}, 'today': {'temperature': '14℃~19℃', 'weather': '晴', 'weather_id': {'fa': '00', 'fb': '00'}, 'wind': '西北风微风', 'week': '星期六', 'city': '上海', 'date_y': '2018年10月27日', 'dressing_index': '较舒适', 'dressing_advice': '建议着薄外套、开衫牛仔衫裤等服装。年老体弱者应适当添加衣物，宜着夹克衫、薄毛衣等。', 'uv_index': '中等', 'comfort_index': '', 'wash_index': '较适宜', 'travel_index': '较适宜', 'exercise_index': '较适宜', 'drying_index': ''}, 'future': {'day_20181027': {'temperature': '14℃~19℃', 'weather': '晴', 'weather_id': {'fa': '00', 'fb': '00'}, 'wind': '西北风微风', 'week': '星期六', 'date': '20181027'}, 'day_20181028': {'temperature': '12℃~22℃', 'weather': '晴', 'weather_id': {'fa': '00', 'fb': '00'}, 'wind': '西风微风', 'week': '星期日', 'date': '20181028'}, 'day_20181029': {'temperature': '14℃~23℃', 'weather': '晴', 'weather_id': {'fa': '00', 'fb': '00'}, 'wind': '西北风3-5级', 'week': '星期一', 'date': '20181029'}, 'day_20181030': {'temperature': '11℃~19℃', 'weather': '晴', 'weather_id': {'fa': '00', 'fb': '00'}, 'wind': '东南风微风', 'week': '星期二', 'date': '20181030'}, 'day_20181031': {'temperature': '11℃~20℃', 'weather': '多云', 'weather_id': {'fa': '01', 'fb': '01'}, 'wind': '南风微风', 'week': '星期三', 'date': '20181031'}, 'day_20181101': {'temperature': '14℃~23℃', 'weather': '晴', 'weather_id': {'fa': '00', 'fb': '00'}, 'wind': '西北风3-5级', 'week': '星期四', 'date': '20181101'}, 'day_20181102': {'temperature': '11℃~19℃', 'weather': '晴', 'weather_id': {'fa': '00', 'fb': '00'}, 'wind': '东南风微风', 'week': '星期五', 'date': '20181102'}}}, 'error_code': 0}"
        hope = "successed!"
        # 包含断言
        self.assertIn(hope, result, "实际结果和预期结果不一致")
        a = 1
        b = 1
        # 相等断言
        self.assertEqual(a, b, "实际结果和预期结果不一致")

        print("测试pass")

    def testAdd02(self):
        '''
               用例描述：cityname 传入空
               期望结果：reason 返回 error or
               '''






if __name__ == '__main__':
    unittest.main()
