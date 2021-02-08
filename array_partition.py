def arrayPairSum(nums) -> int:
    """
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

    Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
    >>> arrayPairSum([1,4,3,2])
    4
    >>> arrayPairSum([6,2,6,5,1,2])
    9
    """
    return sum(sorted(nums)[:-1][::-2])


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
