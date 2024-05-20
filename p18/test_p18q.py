import p18q


def test_solve():
    assert 23 == p18q.solve([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]])

    grid = [
        [int(number) for number in line.strip().split()]
        for line in open("./p18/input.txt").readlines()
    ]
    assert 1074 == p18q.solve(grid)
