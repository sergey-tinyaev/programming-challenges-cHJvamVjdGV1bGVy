import p11q


def test_solve():
    grid = [
        [int(number) for number in line.strip().split()]
        for line in open("./p11/input.txt").readlines()
    ]
    assert 70600674 == p11q.solve(grid)
