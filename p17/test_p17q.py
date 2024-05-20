import p17q


def test_count_letters():
    assert 3 == p17q.count_letters(1)  # one
    assert 3 == p17q.count_letters(2)  # two
    assert 5 == p17q.count_letters(3)  # three
    assert 4 == p17q.count_letters(4)  # four
    assert 4 == p17q.count_letters(5)  # five
    assert 3 == p17q.count_letters(10)  # ten
    assert 6 == p17q.count_letters(11)  # eleven
    assert 6 == p17q.count_letters(12)  # twelve
    assert 8 == p17q.count_letters(13)  # thirteen
    assert 8 == p17q.count_letters(14)  # fourteen
    assert 7 == p17q.count_letters(15)  # fifteen
    assert 7 == p17q.count_letters(16)  # sixteen
    assert 9 == p17q.count_letters(17)  # seventeen
    assert 8 == p17q.count_letters(18)  # eighteen
    assert 8 == p17q.count_letters(19)  # nineteen
    assert 6 == p17q.count_letters(20)  # twenty
    assert 6 + 3 == p17q.count_letters(21)  # twenty one
    assert 6 + 4 == p17q.count_letters(25)  # twenty five
    assert 6 + 3 == p17q.count_letters(32)  # thirty two
    assert 5 + 5 == p17q.count_letters(58)  # fifty eight
    assert 5 + 4 == p17q.count_letters(64)  # sixty four
    assert 7 + 4 == p17q.count_letters(79)  # seventy nine
    assert 6 + 5 == p17q.count_letters(83)  # eighty three
    assert 6 + 4 == p17q.count_letters(99)  # ninety nine
    assert 3 + 7 == p17q.count_letters(100)  # one hundred
    assert 3 + 7 + 3 + 3 == p17q.count_letters(101)  # one hundred and one
    assert 3 + 7 + 3 + 3 == p17q.count_letters(110)  # one hundred and ten
    assert 3 + 7 + 3 + 7 == p17q.count_letters(115)  # one hundred and fifteen
    assert 3 + 7 + 3 + 9 == p17q.count_letters(117)  # one hundred and seventeen
    assert 3 + 7 + 3 + 6 == p17q.count_letters(120)  # one hundred and twenty
    assert 3 + 7 + 3 + 5 + 3 == p17q.count_letters(152)  # one hundred and fifty two
    assert 3 + 7 + 3 + 5 == p17q.count_letters(208)  # two hundred and eight
    assert 5 + 7 == p17q.count_letters(300)  # three hundred
    assert 5 + 7 + 3 + 5 + 3 == p17q.count_letters(342)  # three hundred and forty two
    assert 5 + 7 + 3 + 6 + 4 == p17q.count_letters(394)  # three hundred and ninety four
    assert 4 + 7 + 3 + 8 == p17q.count_letters(513)  # five hundred and thirteen
    assert 4 + 7 + 3 + 6 + 4 == p17q.count_letters(999)  # nine hundred and ninety nine
    assert 3 + 8 == p17q.count_letters(1000)  # one thousand


def test_solve():
    assert 3 == p17q.solve(1)
    assert 3 + 3 + 5 + 4 + 4 == p17q.solve(5)
    assert 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4 + 3 == p17q.solve(10)
    assert (
        3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4 + 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8 + 6
    ) == p17q.solve(20)
    assert 864 == p17q.solve(100)
    assert 21124 == p17q.solve(1000)
