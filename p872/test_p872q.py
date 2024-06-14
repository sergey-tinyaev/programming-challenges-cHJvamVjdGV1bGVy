import p872q


def test_solve():
    assert 12 == p872q.solve(6, 1)
    assert 29 == p872q.solve(10, 3)
    assert 2903144925319290239 == p872q.solve(10**17, 9**17)
