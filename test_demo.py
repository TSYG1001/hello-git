"""一个最小示例：函数 + 对应的测试。

pytest 会自动发现 test_ 开头的函数，不需要 __main__。
"""


def add(a: int, b: int) -> int:
    return a + b


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0



def multiply(a: int, b: int) -> int:
    return a * b


def test_multiply():
    assert multiply(2, 3) == 6
