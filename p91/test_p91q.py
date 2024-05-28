import p91q


def test_solve():
    assert 0 == p91q.solve(0)
    assert 3 == p91q.solve(1)
    assert 14 == p91q.solve(2)
    assert 14234 == p91q.solve(50)
