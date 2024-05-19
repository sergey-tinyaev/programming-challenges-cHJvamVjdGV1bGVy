import p5q


def test_solve():
    assert 1 == p5q.solve(1)
    assert 2520 == p5q.solve(10)
    assert 232792560 == p5q.solve(20)
