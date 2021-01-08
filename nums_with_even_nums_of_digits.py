def findNumbers(nums) -> int:
    """
    Given an array nums of integers, return how many of them contain an even number of digits.

    >>> findNumbers([12,345,2,6,7896])
    2
    >>> findNumbers([555,901,482,1771])
    1

    """
    return len([num for num in nums if len(str(num))%2 == 0])


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)