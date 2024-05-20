import p15q


def test_solve():
    assert 2 == p15q.solve(1)
    assert 6 == p15q.solve(2)
    assert 184756 == p15q.solve(10)
    assert 137846528820 == p15q.solve(20)
