LETTER_COUNT_BY_DIGIT = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
LETTER_COUNT_BY_TENS = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
LETTER_COUNT_BY_ORDER = [0, 3, 7, 8]
SPECIAL_CASES = {11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8}


def count_letters(n: int) -> int:
    """Return number of letters in British spelling of n."""
    # Time: O(lg(n)).
    # Space: O(1).
    if n == 0:
        return 4

    result = 0
    if 1000 <= n:
        result += LETTER_COUNT_BY_DIGIT[n // 1000] + LETTER_COUNT_BY_ORDER[3]
        n %= 1000

    if 100 <= n < 1000:
        result += LETTER_COUNT_BY_DIGIT[n // 100] + LETTER_COUNT_BY_ORDER[2]
        n %= 100
        if n:
            result += 3

    if 10 <= n < 100:
        if n in SPECIAL_CASES:
            result += SPECIAL_CASES[n]
            n = 0
        else:
            result += LETTER_COUNT_BY_TENS[n // 10]
            n %= 10

    if 0 < n < 10:
        result += LETTER_COUNT_BY_DIGIT[n]

    return result


def solve(n: int) -> int:
    """Return number of letters in British spelling of numbers in range [1..n]."""
    # Time: O(n * lg(n)).
    # Space: O(1).
    return sum(map(count_letters, range(1, n + 1)))
