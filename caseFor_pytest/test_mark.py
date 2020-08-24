"""
自定义mark
pytest 可以支持自定义标记，自定义标记可以把一个 web 顷目划分多个模块，然后指定模块名称执行。app 自动化的时候，如果想
android 呾 ios 公用一套代码时，可以使用标记功能，标明哪些是 ios 用例，哪些是 android 的，运行代码时候指定 mark 名称运行就可以
pytest  -m=webtest test_mark.py
pytest  -m "not webtest" test_mark.py

"""
import pytest


@pytest.mark.interfacetest
def test_one():
    assert 1 == 1


@pytest.mark.webtest
def test_two():
    assert 1 == 2


if __name__ == '__main__':
    pytest.main()