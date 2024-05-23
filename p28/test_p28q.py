import p28q


def test_solve():
    assert 1 == p28q.solve(1)
    assert 25 == p28q.solve(3)
    assert 101 == p28q.solve(5)
    assert 261 == p28q.solve(7)
    assert 669171001 == p28q.solve(1001)
