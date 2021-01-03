def numberOfSteps(num: int, steps=0) -> int:
    """
Given a non-negative integer num, return the number of steps to reduce it to zero.

If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

    >>> numberOfSteps(14)
    6
    >>> numberOfSteps(8)
    4
    >>> numberOfSteps(123)
    12

    """
    if num == 0:
        return steps
    if num % 2 == 0:
        steps += 1
        return numberOfSteps(num // 2, steps)
    if num % 2 == 1:
        steps += 1
        return numberOfSteps(num - 1, steps)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
