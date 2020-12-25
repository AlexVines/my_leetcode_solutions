def runningSum(nums):
    """
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

    Return the running sum of nums.
    >>> runningSum([1,2,3,4])
    [1, 3, 6, 10]
    >>> runningSum([1,1,1,1,1])
    [1, 2, 3, 4, 5]
    >>> runningSum([3,1,2,10,1])
    [3, 4, 6, 16, 17]

    """
    for i in range(len(nums)-1):
        nums[i+1] = nums[i] + nums[i+1]
    return nums


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)