def subtractProductAndSum(n):
    """
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

    Return the running sum of nums.
    >>> subtractProductAndSum(234)
    15
    >>> subtractProductAndSum(4421)
    21

    """
    digits = [int(digit) for digit in str(n)]
    mult = 1
    summ = 0
    for d in digits:
        mult *= d
        summ += d
    return mult - summ


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)



