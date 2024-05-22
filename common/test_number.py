import number


def test_get_digits():
    assert [0] == number.get_digits(0)
    assert [1] == number.get_digits(1)
    assert [2] == number.get_digits(2)
    assert [1, 0] == number.get_digits(10)
    assert [1, 1] == number.get_digits(11)
    assert [9, 9] == number.get_digits(99)
    assert [1, 0, 0] == number.get_digits(100)
    assert [1, 9, 9, 0] == number.get_digits(1990)
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] == number.get_digits(1234567890)
    assert [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] == number.get_digits(9876543210)
    assert [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] == number.get_digits(10**12)


def test_sum_of_digits():
    assert 0 == number.sum_of_digits(0)
    assert (
        1
        == number.sum_of_digits(1)
        == number.sum_of_digits(10)
        == number.sum_of_digits(10**2)
        == number.sum_of_digits(10**12)
    )
    assert 2 == number.sum_of_digits(2) == number.sum_of_digits(11)
    assert 45 == number.sum_of_digits(1234567890) == number.sum_of_digits(9876543210)
