"""
场景：用例1需要先登录。 用例2不需要登录。 用例3需要先登录。 该场景下无法使用setup和teardown方式实现。
解决: 自定义测试用例预置条件 （fixture）
"""
import pytest


# 多个文件中都要自定义fixture的话，都需要则在目录下建立conftest.py文件(要和用例在定义package下)定义@pytest.fixture。既可以在多个用例中调用，无须import
def test_c1(login):  # 传入login
    print("用例1：登录后其他动作222")


def test_c2():
    print("用例2不需要登录，操作333")


if __name__ == '__main__':
    pytest.main("-s")
