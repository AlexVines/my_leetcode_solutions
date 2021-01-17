def generateTheString(n: int) -> str:
    """
    Given an integer n, return a string with n characters such that each character in such string occurs an odd number
    of times.

    The returned string must contain only lowercase English letters. If there are multiples valid strings,
    return any of them.

    >>> generateTheString(4)
    'baaa'
    >>> generateTheString(2)
    'ba'
    >>> generateTheString(7)
    'aaaaaaa'

    """
    if n % 2 == 0:
        res = 'b'
    else:
        res = 'a'
    return res + 'a' * (n - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)