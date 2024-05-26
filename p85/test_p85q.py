import p85q


def test_solve():
    assert 1 == p85q.solve(1)
    assert 2 == p85q.solve(3)
    assert 6 == p85q.solve(18)
    assert 22 == p85q.solve(200)
    assert 230 == p85q.solve(20_000)
    assert 2772 == p85q.solve(2_000_000)
