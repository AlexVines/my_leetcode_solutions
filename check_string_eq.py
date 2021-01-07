def arrayStringsAreEqual(word1, word2) -> bool:
    """
    Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

    A string is represented by an array if the array elements concatenated in order forms the string.
    >>> arrayStringsAreEqual(["ab", "c"], ["a", "bc"])
    True
    >>> arrayStringsAreEqual(["a", "cb"], ["ab", "c"])
    False
    >>> arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"])
    True

    """
    return ''.join(word1) == ''.join(word2)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
