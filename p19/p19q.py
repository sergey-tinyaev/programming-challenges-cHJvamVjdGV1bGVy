ADJUSTMENT_BY_MONTH = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
ADJUSTMENT_BY_MONTH_LEAP_YEAR = [3, 1, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]


def is_leap_year(year: int) -> bool:
    """Return whether target year is leap."""
    # Time: O(1).
    # Space: O(1).
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))


def sunday_count(target_year: int) -> int:
    """Return number of times Sunday fell on the first of the month from Jan 1, 1900
    till Jan 1 of the target year."""
    # Time: O(n), where n - number of months between two dates.
    # Space: O(1).
    x, result = 6, 0

    for year in range(1900, target_year):
        adjustments = (
            ADJUSTMENT_BY_MONTH_LEAP_YEAR if is_leap_year(year) else ADJUSTMENT_BY_MONTH
        )
        for adjustment in adjustments:
            x = (x - adjustment) % 7
            if x == 0:
                result += 1

    if x == 0:
        result -= 1

    return result


def solve() -> int:
    """Return number of times Sunday fell on the first of the month from Jan 1, 1901
    till Dec 31, 2000."""
    # Time complexity: O(1) - because arguments are fixed.
    # Extra space complexity: O(1)
    return sunday_count(2001) - sunday_count(1901)
