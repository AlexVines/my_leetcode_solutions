def diagonalSum(mat) -> int:
    """
    Given a square matrix mat, return the sum of the matrix diagonals.

    Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal
    that are not part of the primary diagonal.
    >>> diagonalSum([[1,2,3], [4,5,6], [7,8,9]])
    25
    >>> diagonalSum([[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]])
    8

    """
    length = len(mat[0])
    res = 0
    for i in range(length):
        res += mat[i][i] + mat[length - i - 1][i]
    if length % 2 == 1:
        res -= mat[length // 2][length // 2]
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)