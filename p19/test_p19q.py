import p19q


def test_is_leap_year():
    assert not p19q.is_leap_year(1900)
    assert not p19q.is_leap_year(1901)
    assert not p19q.is_leap_year(1902)
    assert not p19q.is_leap_year(1903)
    assert p19q.is_leap_year(1904)
    assert p19q.is_leap_year(2000)
    assert not p19q.is_leap_year(2001)
    assert not p19q.is_leap_year(2002)
    assert not p19q.is_leap_year(2003)
    assert p19q.is_leap_year(2004)
    assert not p19q.is_leap_year(2005)
    assert not p19q.is_leap_year(2006)
    assert not p19q.is_leap_year(2007)
    assert p19q.is_leap_year(2008)


def test_sunday_count():
    assert 2 == p19q.sunday_count(1901)  # = Apr 1900, Jun 1900
    assert 4 == p19q.sunday_count(1902)  # + Sep 1901, Dec 1901
    assert 5 == p19q.sunday_count(1903)  # + Jun 1902
    assert 8 == p19q.sunday_count(1904)  # + Feb 1903, Mar 1903, Nov 1903
    assert 9 == p19q.sunday_count(1905)  # + May 1904
    assert 11 == p19q.sunday_count(1906)  # + Jan 1905, Oct 1905


def test_solve():
    assert 171 == p19q.solve()
