import q


def test_asum():
    assert 1 == q.asum(10**0)
    assert 55 == q.asum(10**1)
    assert 5050 == q.asum(10**2)
    assert 500500 == q.asum(10**3)
    assert 50005000 == q.asum(10**4)
    assert 5000050000 == q.asum(10**5)
    assert 500000500000 == q.asum(10**6)
    assert 50000005000000 == q.asum(10**7)
    assert 5000000050000000 == q.asum(10**8)
    assert 500000000500000000 == q.asum(10**9)
    assert 50000000005000000000 == q.asum(10**10)
    assert 5000000000050000000000 == q.asum(10**11)
    assert 500000000000500000000000 == q.asum(10**12)
    assert 50000000000005000000000000 == q.asum(10**13)
    assert 5000000000000050000000000000 == q.asum(10**14)
    assert 500000000000000500000000000000 == q.asum(10**15)


def test_solve():
    assert 23 == q.solve(10)
    assert 233168 == q.solve(1000)
