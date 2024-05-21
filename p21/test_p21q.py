import p21q


def test_calc_sum_of_proper_divisors():
    primes = [2, 3, 5, 7, 11, 13, 17]
    assert 1 == p21q.sum_of_proper_divisors(2, primes)
    assert 284 == p21q.sum_of_proper_divisors(220, primes)
    assert 220 == p21q.sum_of_proper_divisors(284, primes)


def test_solve():
    assert 31626 == p21q.solve(10000)
