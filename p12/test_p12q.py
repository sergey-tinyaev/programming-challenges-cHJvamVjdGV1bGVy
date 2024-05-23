import math
import common.generator as cg
import p12q


def test_count_divisors():
    primes = list(cg.primes(1 + math.ceil(math.sqrt(5400))))
    assert 1 == p12q.count_divisors(1, primes)
    assert 2 == p12q.count_divisors(2, primes)
    assert 2 == p12q.count_divisors(3, primes)
    assert 4 == p12q.count_divisors(6, primes)
    assert 6 == p12q.count_divisors(28, primes)
    assert 48 == p12q.count_divisors(5400, primes)


def test_solve():
    assert 28 == p12q.solve(5)
    assert 76576500 == p12q.solve(500)
