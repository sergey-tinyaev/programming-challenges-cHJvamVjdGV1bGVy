import p16q


def test_sum_of_digits():
    assert 0 == p16q.sum_of_digits(0)
    assert 1 == p16q.sum_of_digits(1)
    assert 1 == p16q.sum_of_digits(10)
    assert 1 == p16q.sum_of_digits(100)
    assert 9 == p16q.sum_of_digits(45)
    assert 45 == p16q.sum_of_digits(1234567890)


def test_solve():
    assert 26 == p16q.solve(15)
    assert 1366 == p16q.solve(1000)
