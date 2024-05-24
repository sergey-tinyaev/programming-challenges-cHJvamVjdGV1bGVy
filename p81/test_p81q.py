import p81q


def test_solve():
    grid1 = [
        [1, 2],
        [3, 4],
    ]
    assert 7 == p81q.solve(grid1)

    grid2 = [
        [131, 673, 234, 103, 18],
        [201, 96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37, 331],
    ]
    assert 2427 == p81q.solve(grid2)

    grid3 = [
        [int(n) for n in line.strip().split(",")]
        for line in open("./p81/input.txt").readlines()
    ]
    assert 427337 == p81q.solve(grid3)
