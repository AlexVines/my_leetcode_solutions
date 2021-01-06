def balancedStringSplit(s: str) -> int:
    """
    Balanced strings are those who have equal quantity of 'L' and 'R' characters.

    Given a balanced string s split it in the maximum amount of balanced strings.

    Return the maximum amount of splitted balanced strings.

    >>> balancedStringSplit("RLRRLLRLRL")
    4
    >>> balancedStringSplit("RLLLLRRRLR")
    3
    >>> balancedStringSplit("LLLLRRRR")
    1
    >>> balancedStringSplit("RLRRRLLRLL")
    2

    """
    c = 0
    res = 0
    for char in s:
        if char == 'R':
            c += 1
        if char == 'L':
            c -= 1
        if c == 0:
            res += 1
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)