def sortArrayByParity(nums):
    """
    Given an array A of non-negative integers, return an array consisting of all the even elements of A,
    followed by all the odd elements of A.

    You may return any answer array that satisfies this condition.

    >>> sortArrayByParity([3,1,2,4])
    [2, 4, 3, 1]

    """
    length = len(nums)
    i = 0
    res = [None] * length
    for num in nums:
        if num % 2 == 0:
            res[i] = num
            i += 1
    for num in nums:
        if num % 2 == 1:
            res[i] = num
            i += 1
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)