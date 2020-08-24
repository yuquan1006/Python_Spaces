"""
场景：用例1需要先登录。 用例2不需要登录。 用例3需要先登录。 该场景下无法使用setup和teardown方式实现。
解决: 自定义测试用例预置条件 （fixture）

调用fixture三种方法：
1 函数或类里面方法直接传fixture的函数参数名称
2 使用装饰器@pytest.mark,userfixtures()修饰
3 autouser=Ture自动使用

@pytest.fixture(scope="function"）中scope=参数如下：
    - function 每一个函数或方法都会调用
    - class  每一个类调用一次，一个类可以有多个方法
    - module，每一个.py文件调用一次，该文件内又有多个function和class
    - session 是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
"""
import pytest

# 单个测试用例文件中写法如下。如多个都需要则在目录下建立conftest.py文件(要和用例在定义package下)定义@pytest.fixture。既可以在多个用例中调用
@pytest.fixture(scope="function", autouse=True)
def login():
    print("输入账户密码登录")


@pytest.fixture(scope="module", autouse=True)  # module全局一个测试文件中只会执行一次，不管调用几次
def open():
    print("打开浏览器")
    yield
    print("执行teardown,最后关闭浏览器")

def test_c1(login):  # 传入login
    print("用例1：登录后其他动作222")


def test_c2():
    print("用例2不需要登录，操作333")

@pytest.mark.usefixtures("login")
def test_c3():
    print("用例3需要登录，操作333")

@pytest.mark.usefixtures("login")
class TestCase():
    def test_five(self,login):
        x = "york"
        assert "o" in x

    def test_333(self):
        x = "york"
        assert "o" in x

if __name__ == '__main__':
    pytest.main("-s")
