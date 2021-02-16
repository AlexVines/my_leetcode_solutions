def canMakeArithmeticProgression(arr) -> bool:
    """
    Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between
    any two consecutive elements is the same.

    Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.

    >>> canMakeArithmeticProgression([3,5,1])
    True
    >>> canMakeArithmeticProgression([1,2,4])
    False
    """
    arr = sorted(arr)
    diff = arr[0] - arr[1]
    for i in range(len(arr) - 1):
        if arr[i] - arr[i + 1] != diff:
            return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
