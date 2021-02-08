def arrayPairSum(nums) -> int:
    """
    Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
    such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
    >>> arrayPairSum([1,4,3,2])
    4
    >>> arrayPairSum([6,2,6,5,1,2])
    9
    """
    return sum(sorted(nums)[:-1][::-2])


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
