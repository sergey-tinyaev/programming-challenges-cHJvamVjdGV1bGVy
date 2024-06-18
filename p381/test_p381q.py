import p381q


def test_solve():
    assert 480 == p381q.solve(100)
    assert 139602943319822 == p381q.solve(10**8)
