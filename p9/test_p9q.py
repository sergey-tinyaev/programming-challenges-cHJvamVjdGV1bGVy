import p9q


def test_solve():
    assert 3 * 4 * 5 == p9q.solve(12)
    assert 200 * 375 * 425 == p9q.solve(1000)
