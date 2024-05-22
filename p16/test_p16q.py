import p16q


def test_solve():
    assert 26 == p16q.solve(15)
    assert 1366 == p16q.solve(1000)
