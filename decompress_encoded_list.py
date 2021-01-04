def decompressRLElist(nums):
    """
    We are given a list nums of integers representing a list compressed with run-length encoding.

    Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).
    For each such pair, there are freq elements with value val concatenated in a sublist.
    Concatenate all the sublists from left to right to generate the decompressed list.

    Return the decompressed list.

    >>> decompressRLElist([1,2,3,4])
    [2, 4, 4, 4]
    >>> decompressRLElist([1,1,2,3])
    [1, 3, 3]

    """
    res = []
    i = 0
    while i < len(nums):
        res += [nums[i + 1]] * nums[i]
        i += 2
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
