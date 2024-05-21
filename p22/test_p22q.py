import p22q


def test_alpha_sum():
    assert 53 == p22q.alpha_sum("COLIN")
    assert 57 == p22q.alpha_sum("MARY")
    assert 35 == p22q.alpha_sum("ZED")


def test_solve():
    assert 53 == p22q.solve(["COLIN"])
    assert 57 == p22q.solve(["MARY"])
    assert 167 == p22q.solve(["COLIN", "MARY"])
    assert 35 == p22q.solve(["ZED"])
    assert 272 == p22q.solve(["COLIN", "MARY", "ZED"])

    data = [line[1:-1] for line in open("./p22/input.txt").read().strip().split(",")]
    assert 871198282 == p22q.solve(data)
