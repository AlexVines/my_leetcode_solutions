def restoreString(s: str, indices) -> str:
    """
    Given a string s and an integer array indices of the same length.

    The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
    
    Return the shuffled string.

    >>> restoreString("codeleet", [4,5,6,7,0,2,1,3])
    'leetcode'
    >>> restoreString("abc", [0,1,2])
    'abc'
    >>> restoreString("aiohn", [3,1,4,2,0])
    'nihao'
    >>> restoreString("aaiougrt", [4,0,2,6,7,3,1,5])
    'arigatou'
    >>> restoreString("art", [1,0,2])
    'rat'
    """

    res = [None] * len(s)
    for i, p in enumerate(indices):
        res[p] = s[i]
    return ''.join(res)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)