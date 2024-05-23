import p8q


def test_solve():
    number = "".join(map(str.strip, open("./p8/input.txt").readlines()))

    assert 5832 == p8q.solve(number, 4)
    assert 23514624000 == p8q.solve(number, 13)
