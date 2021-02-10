def sortedSquares(nums):
    """
    Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted
    in non-decreasing order.
    
    >>> sortedSquares([-4,-1,0,3,10])
    [0, 1, 9, 16, 100]
    >>> sortedSquares([-7,-3,2,3,11])
    [4, 9, 9, 49, 121]
    """
    l = 0
    r = len(nums) - 1
    result = []
    while l <= r:
        if abs(nums[r]) >= abs(nums[l]):
            result.append(nums[r] ** 2)
            r -= 1
        else:
            result.append(nums[l] ** 2)
            l += 1
    return result[::-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)