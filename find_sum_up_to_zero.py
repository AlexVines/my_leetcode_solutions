def sumZero(n: int):
    """
    Given an integer n, return any array containing n unique integers such that they add up to 0.
    >>> sumZero(3)
    [-2, 0, 2]
    >>> sumZero(1)
    [0]
    >>> sumZero(5)
    [-4, -2, 0, 2, 4]

    """
    return list(range(1 - n, n, 2))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)