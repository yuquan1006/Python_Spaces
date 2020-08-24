"""
跳过用例
pytest.mark.skip 可以标记无法在某些平台上运行的测试功能，或者您希望失败的测试功能
使用场景1：跳过测试函数的最简单方法是使用跳过装饰器标记它，可以传递一个可选的原因,示例 test_two()
使用场景2：通过调用来在测试执行或设置期间强制跳过pytest.skip（reason）功能：
使用场景3：pytest.skip（reason，allow_module_level = True）跳过整个模块级别

可以在模块之间共享skipif标记,您可以导入标记并在另一个测试模块中重复使用它：对于较大的测试套件，通常最好有一个文件来定义标记，然后一致适用于整个测试套件。
如果要跳过模块的所有测试功能，可以在全局级别使用pytestmark名称 pytestmark = pytest.mark.skipif(1 > 0, reason="全文件跳过")

skip类或模块,您可以在类上使用skipif标记（与任何其他标记一样）：如果条件为True，则此标记将为该类的每个测试方法生成跳过结果.警告：强烈建议不要在使用继承的类上使用skipif。
 pytest中的一个已知错误标记可能会导致超类中的意外行为。

"""
import pytest, sys
from caseFor_pytest.skips import cat
from caseFor_pytest.test_demo1 import func

# if not func(0):
#     pytest.skip(" skipping tests", allow_module_level=True)

pytestmark = pytest.mark.skipif(1 > 0, reason="全文件跳过")


def f():
    pass

@pytestmark
@pytest.mark.skipif(sys.version_info < (3, 7), reason="python build low!")
def test_one():
    assert 1 == 1


@pytest.mark.skip(reason="f()函数 还未开发完成。")
def test_two():
    assert f() == 3


def test_three():
    if not f():
        pytest.skip("f() 函数，还未开发完成")
    pass

@cat
def test_five():
    assert 1 == 2


def test_xx():
    assert 2 == 2


@pytest.mark.skipif(sys.platform == 'win32', reason="does not run on windows")
class Test_xxz:

    def test_bb(self):
        assert 2 == 2


if __name__ == '__main__':
    pytest.main()