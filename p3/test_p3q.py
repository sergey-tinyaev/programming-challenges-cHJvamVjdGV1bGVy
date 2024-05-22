import p3q


def test_solve():
    assert 29 == p3q.solve(13195)
    assert 6857 == p3q.solve(600851475143)
    assert 10000000019 == p3q.solve(10000000019)
