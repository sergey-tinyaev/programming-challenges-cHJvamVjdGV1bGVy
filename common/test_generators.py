import generator


def test_primes():
    assert [2] == list(generator.primes(2))
    assert [2, 3, 5] == list(generator.primes(5))
    assert 31 == list(generator.primes(50))[10]
    assert 547 == list(generator.primes(5000))[100]
    assert 1229 == list(generator.primes(5000))[200]
    assert 3469 == list(generator.primes(5000))[486]
    assert 4999 == list(generator.primes(5000))[668]
    assert [
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
    ] == list(generator.primes(47))
