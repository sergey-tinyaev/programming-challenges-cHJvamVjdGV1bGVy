import p13q


def test_advance():
    assert 40 == p13q.advance(13)
    assert 20 == p13q.advance(40)
    assert 10 == p13q.advance(20)
    assert 5 == p13q.advance(10)
    assert 16 == p13q.advance(5)
    assert 8 == p13q.advance(16)
    assert 4 == p13q.advance(8)
    assert 2 == p13q.advance(4)
    assert 1 == p13q.advance(2)


def test_walk():
    assert 1 == p13q.walk(1, {1: 1})
    assert 2 == p13q.walk(2, {1: 1})
    assert 10 == p13q.walk(13, {1: 1})

    # make sure it uses provided cache
    assert 2 == p13q.walk(13, {40: 1})


def test_solve():
    assert 9 == p13q.solve(10)
    assert 97 == p13q.solve(100)
    assert 871 == p13q.solve(1_000)
    assert 6171 == p13q.solve(10_000)
    assert 77031 == p13q.solve(100_000)
    assert 837799 == p13q.solve(1_000_000)
