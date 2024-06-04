import p62q


def test_solve():
    assert 1 == p62q.solve(1)
    assert 125 == p62q.solve(2)
    assert 41063625 == p62q.solve(3)
    assert 1006012008 == p62q.solve(4)
    assert 127035954683 == p62q.solve(5)
