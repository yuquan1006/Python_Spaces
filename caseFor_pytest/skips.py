import pytest

cat = pytest.mark.skipif(1 > 0, reason="暂不执行")

