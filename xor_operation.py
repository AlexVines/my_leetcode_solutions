def xorOperation(n: int, start: int) -> int:
    """
    Given an integer n and an integer start.

    Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

    Return the bitwise XOR of all elements of nums

    >>> xorOperation(5, 0)
    8
    >>> xorOperation(4, 3)
    8
    >>> xorOperation(1, 7)
    7
    >>> xorOperation(10, 5)
    2

    """
    res = start
    for i in range(1, n):
        res = res ^ (start + i * 2)
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)



