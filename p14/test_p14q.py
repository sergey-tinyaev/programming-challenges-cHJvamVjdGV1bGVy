import p14q


def test_advance():
    assert 40 == p14q.advance(13)
    assert 20 == p14q.advance(40)
    assert 10 == p14q.advance(20)
    assert 5 == p14q.advance(10)
    assert 16 == p14q.advance(5)
    assert 8 == p14q.advance(16)
    assert 4 == p14q.advance(8)
    assert 2 == p14q.advance(4)
    assert 1 == p14q.advance(2)


def test_walk():
    assert 1 == p14q.walk(1, {1: 1})
    assert 2 == p14q.walk(2, {1: 1})
    assert 10 == p14q.walk(13, {1: 1})

    # make sure it uses provided cache
    assert 2 == p14q.walk(13, {40: 1})


def test_solve():
    assert 9 == p14q.solve(10)
    assert 97 == p14q.solve(100)
    assert 871 == p14q.solve(1_000)
    assert 6171 == p14q.solve(10_000)
    assert 77031 == p14q.solve(100_000)
    assert 837799 == p14q.solve(1_000_000)
