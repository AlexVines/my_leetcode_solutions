def canBeEqual(target, arr) -> bool:
    """
    Given two integer arrays of equal length target and arr.

    In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.

    Return True if you can make arr equal to target, or False otherwise.
    >>> canBeEqual([1,2,3,4], [2,4,1,3])
    True
    >>> canBeEqual([7], [7])
    True
    >>> canBeEqual([1,12], [12 ,1])
    True
    >>> canBeEqual([3, 7, 9], [3, 7, 11])
    False
    >>> canBeEqual([1, 1, 1, 1, 1], [1, 1, 1, 1, 1])
    True
    """
    return sorted(target) == sorted(arr)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
