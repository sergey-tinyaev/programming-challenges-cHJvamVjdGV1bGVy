import p12q


# def test_count_prime_freq():
#     assert {} == p12q.count_prime_freq(1)
#     assert {2: 1} == p12q.count_prime_freq(2)
#     assert {3: 1} == p12q.count_prime_freq(3)
#     assert {2: 1, 3: 1} == p12q.count_prime_freq(6)
#     assert {2: 2, 7: 1} == p12q.count_prime_freq(28)
#     assert {2: 3, 3: 3, 5: 2} == p12q.count_prime_freq(5400)


def test_count_divisors():
    assert 1 == p12q.count_divisors(1)
    assert 2 == p12q.count_divisors(2)
    assert 2 == p12q.count_divisors(3)
    assert 4 == p12q.count_divisors(6)
    assert 6 == p12q.count_divisors(28)
    assert 48 == p12q.count_divisors(5400)


def test_solve():
    assert 28 == p12q.solve(5)
    assert 76576500 == p12q.solve(500)
