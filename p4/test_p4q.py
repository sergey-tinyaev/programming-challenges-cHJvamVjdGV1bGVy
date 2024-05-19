import p4q


def test_solve():
    assert 9009 == p4q.solve(2, 2)
    assert 94149 == p4q.solve(2, 3) == p4q.solve(3, 2)
    assert 906609 == p4q.solve(3, 3)
    assert 99000099 == p4q.solve(4, 4)
