import p148q


def test_solve():
    assert 1 == p148q.solve(1)
    assert 6 == p148q.solve(3)
    assert 28 == p148q.solve(7)
    assert 2361 == p148q.solve(100)
    assert 118335 == p148q.solve(1_000)
    assert 14938429440 == p148q.solve(1_000_000)
    assert 2129970655314432 == p148q.solve(1_000_000_000)
