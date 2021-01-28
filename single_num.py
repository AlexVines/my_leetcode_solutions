def singleNumber(nums) -> int:
    """
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

    Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
    >>> singleNumber([2,2,1])
    1
    >>> singleNumber([4,1,2,1,2])
    4
    >>> singleNumber([1])
    1

    """
    a = 0
    for i in nums:
        a ^= i
    return a


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)