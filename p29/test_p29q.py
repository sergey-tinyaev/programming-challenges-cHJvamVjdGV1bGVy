import p29q


def test_solve():
    assert 1 == p29q.solve(2)
    assert 4 == p29q.solve(3)
    assert 8 == p29q.solve(4)
    assert 15 == p29q.solve(5)
    assert 23 == p29q.solve(6)
    assert 34 == p29q.solve(7)
    assert 44 == p29q.solve(8)
    assert 54 == p29q.solve(9)
    assert 69 == p29q.solve(10)
    assert 88 == p29q.solve(11)
    assert 106 == p29q.solve(12)
    assert 129 == p29q.solve(13)
    assert 152 == p29q.solve(14)
    assert 177 == p29q.solve(15)
    assert 195 == p29q.solve(16)
    assert 226 == p29q.solve(17)
    assert 256 == p29q.solve(18)
    assert 291 == p29q.solve(19)
    assert 324 == p29q.solve(20)
    assert 361 == p29q.solve(21)
    assert 399 == p29q.solve(22)
    assert 442 == p29q.solve(23)
    assert 9183 == p29q.solve(100)