def majorityElement(nums) -> int:
    """
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.

    >>> majorityElement([3,2,3])
    3
    >>> majorityElement([2,2,1,1,1,2,2])
    2
    """
    n = len(nums)
    res = {}
    for num in nums:
        if num in res:
            res[num] += 1
        else:
            res[num] = 1

        if res[num] > n // 2:
            return num


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)