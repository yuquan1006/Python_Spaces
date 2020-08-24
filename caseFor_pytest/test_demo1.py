import pytest
"""
unittest
pytest
用例编写规则
    1)测试文件必须先import unittest
    2)测试类必须继承unittest.TestCase
    3)测试方法必须以“test_”开头
    4)测试类必须要有unittest.main()方法
    1)测试文件名必须以“test_”开头或者"_test"结尾（如：test_ab.py）
    2)测试方法必须以“test_”开头
    3)测试类命名以"Test"开头
 
用例分类执行
    默认执行全部用例，也可以通过加载testsuit，执行部分用例
    可以通过@pytest.mark来标记类和方法，pytest.main加入参数("-m")可以只运行标记的类和方法

用例前置和后置
    提供了setUp/tearDown，只能针对所有用例
    pytest中的fixture显然更加灵活。可以任意自定义方法函数，只要加上@pytest.fixture()这个装饰器，那么被装饰的方法就可以被使用
    
参数化

    需依赖ddt库
    使用@pytest.mark.parametrize装饰器
    
断言
    很多断言格式(assertEqual、assertIn、assertTrue、assertFalse)
    只有assert一个表达式，用起来比较方便
报告
    使用HTMLTestRunnerNew库
    有pytest-HTML、allure插件
失败重跑
    无此功能
    pytest支持用例执行失败重跑，pytest-rerunfailures插件
    
    
执行测试命令：pytest
执行用例规则：
    1 某个目录下所有的用例   pytest 文件名/
    2.执行某一个 py 文件下用例     pytest testxx.py
    
参数: -q  显示简单结果
    -x 遇到错误时停止测试
    --maxfail=num 当用例错诨个数达到指定数量时，停止测试
    -m 指定mark执行 pytest -m webtest test_mark.py 执行标记 webtest 的用例，那就用    ;pytest -m "not webtest" test_mark.py 如果丌想执行标记 webtest 的用例，那就用”not webtest”
    -v 指定的函数节点id  pytest -v test_demo1.py::TestClass::test_one; 多节点 pytest -v test_demo1.py::TestClass::test_one test_demo1.py::test_answer 
    -k 匹配用例名称  pytest -v -k one ; 根据用例名称排除掉某些用例 pytest -v -k "not one"; 多个匹配 pytest -k "one or two"
    --html=report.html  生成测试报告 pytest --html=report.html  --self-contained-html （报告独立显示）  安装插件 pytest-html
    --reruns 1  失败重新执行1次。 安装插件pytest-rerunfailures
    --reruns-delay=RERUNS_DELAY RERUNS_DELAY 是失败后间隔多少 s 重新执行，时间单位是 s
    
pytest+allure生成报告:
    --alluredir report 生成allure的测试报告。安装插件allure-pytest.  pytest --alluredir report 
     allure 生成对应测试报告，安装allure2插件(https://github.com/allure-framework/allure2/releases/tag/2.8.1)。  allure generate report/ -o report/html --clean  


pytest.xfail 将用例标记为失败。 test_answer()
"""

# content of test_sample.py
def func(x):
    return x + 0


def test_answer(a = 0):
    if not a:
        pytest.xfail("登录失败，不执行")
    assert func(3) == 5


class TestClass:
    def test_one(self):
        x = "york"
        assert "o" in x

    def test_two(self):
        x = 12
        assert isinstance(x, list) == True

    def one(self):
        x = "yorks"
        assert "s" in x


if __name__ == '__main__':
    pytest.main()
