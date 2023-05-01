import sum


def test_add1():
    assert sum.sum(1, 2) == 3


def test_add2():
    assert sum.sum(2, 2) == 4


def test_add3():
    x = 1
    y = 2
    z = x + y
    assert sum.sum(z, 2) == 4
