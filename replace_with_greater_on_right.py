def replaceElements(nums):
    """
    Given an array arr, replace every element in that array with the greatest element among the elements to its right,
    and replace the last element with -1.

    After doing so, return the array.

    >>> replaceElements([17,18,5,4,6,1])
    [18, 6, 6, 6, 1, -1]
    >>> replaceElements([400])
    [-1]

    """
    length = len(nums)
    i = length - 1
    res = [None] * length
    big = -1
    while i >= 0:
        res[i] = big
        if nums[i] > big:
            big = nums[i]
        i -= 1
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)