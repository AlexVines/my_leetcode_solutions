def hammingDistance(x: int, y: int) -> int:
    """
    The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

    Given two integers x and y, calculate the Hamming distance.
    
    >>> hammingDistance(1, 4)
    2

    """
    fill = len(bin(max(x, y))) - 2
    xb = bin(x)[2:].zfill(fill)
    yb = bin(y)[2:].zfill(fill)
    res = 0
    for i in range(fill):
        if xb[i] != yb[i]:
            res += 1
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)