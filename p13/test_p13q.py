import p13q


def test_solve():
    assert 3 == p13q.solve(["1", "2"])

    numbers = [line.strip() for line in open("./p13/input.txt").readlines()]
    assert 5537376230390876637302048746832985971773659831892672 == p13q.solve(numbers)
