def solve(n: str, k: int) -> int:
    """Return the largest product of k consecutive digits in n."""
    # Time: O(lg(n)).
    # Space: O(1).
    count, product, result = 0, 1, -1
    for i, ch in enumerate(n):
        digit = ord(ch) - ord("0")
        if digit == 0:
            count, product = 0, 1
        else:
            product *= digit
            if count == k - 1:
                if product > result:
                    result = product
                product //= ord(n[i - count]) - ord("0")
            else:
                count += 1

    return result
