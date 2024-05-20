import p10q


def test_solve():
    assert 17 == p10q.solve(10)
    assert 142913828922 == p10q.solve(2_000_000)
