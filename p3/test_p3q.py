import p3q


def test_gen_primes_up_to():
    assert list(p3q.gen_primes_up_to(2)) == [2]
    assert list(p3q.gen_primes_up_to(3)) == [2, 3]
    assert list(p3q.gen_primes_up_to(47)) == [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
    ]



def test_solve():
    assert 29 == p3q.solve(13195)
    assert 6857 == p3q.solve(600851475143)
    assert 10000000019 == p3q.solve(10000000019)
