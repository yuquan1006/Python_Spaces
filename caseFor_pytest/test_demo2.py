"""
用例运行级别
模块级（setup_module/teardown_module）开始于模块始末，全局的

函数级（setup_function/teardown_function）只对函数用例生效（不在类中）

类级（setup_class/teardown_class）只在类中前后运行一次(在类中)

方法级（setup_method/teardown_method）开始于方法始末（在类中）

类里面的（setup/teardown）运行在调用方法的前后
"""
import pytest


def setup_module():
    print("setup_module：整个.py文件只执行一次。比如所有用例执行前打开一次浏览器")


def teardown_module():
    print("teardown_module：整个.py文件执行一次。比如所有用例执行完关闭浏览器")


def setup_function():
    print("每个函数用例执行前，打印一次")


def teardown_function():
    print("每个函数用例执行后，打印一次")


def test_one():
    print("正在执行test_one")
    assert 1 == 1


def test_two():
    print("正在执行test_two")
    assert 1 == 1

class TestCase():
    def setup(self):
        print("setup:类中每个用例开始前执行")

    def teardown(self):
        print("teardown:类中每个用例结束后执行")

    def setup_class(self):
        print("setup_class:类中所有用例开始前执行")
    def setup_method(self):
        print("setup_method:类中每个用例开始前执行")


    def test_five(self):
        x = "york"
        assert "o" in x

    def test_three(self):
        x = 12
        assert isinstance(x, list) == True

    def one(self):
        x = "yorks"
        assert "s" in x


if __name__ == '__main__':
    pytest.main("-s")