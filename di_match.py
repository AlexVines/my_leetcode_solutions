def diStringMatch(S: str):
    """
    Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

    Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

    If S[i] == "I", then A[i] < A[i+1]
    If S[i] == "D", then A[i] > A[i+1]
    >>> diStringMatch("IDID")
    [0, 4, 1, 3, 2]
    >>> diStringMatch("III")
    [0, 1, 2, 3]
    >>> diStringMatch("DDI")
    [3, 2, 0, 1]

    """
    start = 0
    end = len(S)
    res = []
    for char in S:
        if char == 'I':
            res.append(start)
            start += 1
        else:
            res.append(end)
            end -= 1
    res.append(end)
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)