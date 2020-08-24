# encode:utf-8
import pytest
"""
多个文件中都要自定义fixture的话，都需要则在目录下建立conftest.py文件(要和用例在定义package下)定义@pytest.fixture。既可以在
多个用例中调用，无须import
"""

@pytest.fixture(scope="function")
def login():
    print("输入账户密码登录")


@pytest.fixture(scope="module")  # module全局一个测试文件中只会执行一次，不管调用几次
def open():
    print("打开浏览器")
    yield
    print("执行teardown,最后关闭浏览器")


@pytest.fixture(scope="class")
def bbb():
    print("类级别")