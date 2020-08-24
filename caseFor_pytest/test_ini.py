"""
pytest中配置文件：
    pytest.ini pytest的主配置文件，可以改变pytest的默认行为
    conftest.py 测试用例的一些fixture配置
    _init_.py 识别该文件夹为python的package包
    tox.ini 与pytest.ini类似，用tox工具时候才有用
    setup.cfg 也是ini格式文件，影响setup.py的行为

pytest.ini
[pytest]
;作用一：pytest.ini配置  更改用例匹配规则

;python_files = test_*.py *_test.py     #执行时，会按照这个配置名称开头或结尾的  来查找测试脚本文件
;python_classes = Test*               #执行时，会按照这个配置名称开头的测试类，从而查找这个类下的测试脚本文件
;python_functions = test_*            #执行时，会按照这个配置名称开头的方法来查找


;作用二： 管理自定义mark(即:@pytest.mark.xxx 装饰器)。 pytest --markers（会列出当前工程内所有使用了mark标记的地方）
markers =
    webtest: run webtest testcase
    interfacetest: run interfacetest testcase

作用三：addopts参数，可以更改默认命令行选项.如：在cmd输入指令去执行用例的时候，命令太长，每次执行时都要重复操作很麻烦，那么可以用addopts参数代替使用。
addopts = -v -q -m webtest
此时再进行执行用例时，在命令行中直接输入：pytest，就可以了（会自动在pytest.ini中找到当前已配置的addopts配置信息进行执行）

作用四：cache_dir设置缓存文件路径,执行测试时会默认在执行的路径中生成pytest_cache文件夹，
如果不想在这个地方出现这个文件夹，可以配置存放路径，方便管理
cache_dir=D:\\myCode\\ihr_web\\.pytest_cache

作用五：添加用例路径

把用例所在的目录添加到配置文件，这样在运行用例的时候，pytest会直接在配置文件内指定的 目录  去查找匹配 用例
（因为不写这个路径的话，运行时会按照用例的规则在工程下全局匹配符合条件的用例）
[pytest]
testpaths=./TestCases

"""