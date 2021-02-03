def moveZeroes(nums) -> None:
    """
    Given an array nums, write a function to move all 0's to the end of it while maintaining the
    relative order of the non-zero elements.

    >>> moveZeroes([0,1,0,3,12])
    [1, 3, 12, 0, 0]

    """
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos += 1
    for i in range(pos, len(nums)):
        nums[i] = 0

    return nums
    

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)