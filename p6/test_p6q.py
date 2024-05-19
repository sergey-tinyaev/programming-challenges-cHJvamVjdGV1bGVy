import p6q


def test_solve():
    assert 2640 == p6q.solve(10)
    assert 25164150 == p6q.solve(100)
    assert 250166416500 == p6q.solve(1000)
