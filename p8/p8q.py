DATA = "".join(map(str.strip, open("./p8/input.txt").readlines()))


def solve(n: int) -> int:
    # Time complexity: O(D), where D - number of digits
    # Extra space complexity: O(1)
    count, product, result = 0, 1, -1
    for i, e in enumerate(DATA):
        digit = ord(e) - ord("0")
        if digit == 0:
            count, product = 0, 1
        else:
            product *= digit
            if count == n - 1:
                if product > result:
                    result = product
                product //= ord(DATA[i - count]) - ord("0")
            else:
                count += 1

    return result
