import pytest
import p45q


def test_solve():
    assert 40755 == p45q.solve(1)
    assert 1533776805 == p45q.solve(2)


@pytest.mark.skip(reason="Performance benchmark test.")
def test_solve_performance():
    assert 57722156241751 == p45q.solve(3)


@pytest.mark.skip(reason="Too slow.")
def test_solve_performance2():
    assert 0 == p45q.solve(4)
