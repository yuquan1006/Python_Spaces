import pytest


def test_xx(login):
    print("执行测试0")
    assert 2 == 2


def setup_function():
    print("每个函数用例测试前执行")


def teardown_function():
    print("每个函数用例测试后执行")


def setup_module():
    print("每个py文件执行一次")


@pytest.fixture(scope='function')
def login():
    print("自定义前置；先登录下")
    yield
    print("teardown实现用yield完成。")
    print("自定义后置：xx")


@pytest.fixture(scope='module',autouse=True)
def open():
    print("module全文件中自定义前置只执行一次；打开浏览器")



class TestLogin:


    def setup_method(self):
        print("测试类中每个方法执行前执行一次")


    def setup_class(self):
        print("每个测试类之前执行一次")

    @pytest.mark.usefixtures("login")
    def test_one(self):
        print("执行测试1")
        assert 1 == 2

    def test_two(self):
        print("执行测试2")
        assert "x" in "abc"

    def test_three(self):
        print("执行测试3")
        assert "a" in "abc"


if __name__ == '__main__':
    pytest.main(["-s", "test01.py"])
