import p24q


def test_to_int():
    assert 12 == p24q.to_int((1, 2))
    assert 321 == p24q.to_int((3, 2, 1))
    assert 1234 == p24q.to_int((1, 2, 3, 4))
    assert 54321 == p24q.to_int((5, 4, 3, 2, 1))
    assert 123456 == p24q.to_int((1, 2, 3, 4, 5, 6))
    assert 7654321 == p24q.to_int((7, 6, 5, 4, 3, 2, 1))
    assert 12345678 == p24q.to_int((1, 2, 3, 4, 5, 6, 7, 8))
    assert 987654321 == p24q.to_int((9, 8, 7, 6, 5, 4, 3, 2, 1))
    assert 1234567890 == p24q.to_int((1, 2, 3, 4, 5, 6, 7, 8, 9, 0))


def test_solve():
    assert 123456789 == p24q.solve(1)
    assert 2783915460 == p24q.solve(1_000_000)
