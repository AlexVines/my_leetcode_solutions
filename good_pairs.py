def numIdenticalPairs(nums):
    """
    Given an array of integers nums.

    A pair (i,j) is called good if nums[i] == nums[j] and i < j.

    Return the number of good pairs.

    >>> numIdenticalPairs([1,2,3,1,1,3])
    4
    >>> numIdenticalPairs([1,1,1,1])
    6
    >>> numIdenticalPairs([1,2,3])
    0

    """
    result = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and i < j:
                result += 1
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)



