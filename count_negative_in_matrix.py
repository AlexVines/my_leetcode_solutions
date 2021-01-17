def countNegatives(grid) -> int:

    """
    Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
    return the number of negative numbers in grid.

    >>> countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
    8
    >>> countNegatives([[3,2],[1,0]])
    0
    >>> countNegatives([[1,-1],[-1,-1]])
    3
    >>> countNegatives([[-1]])
    1

    """
    rows = len(grid)
    i = len(grid[0]) - 1
    j = 0
    res = 0
    while i >= 0 and j < rows:
        if grid[j][i] < 0:
            res += rows - j
            i -= 1
        else:
            j += 1
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)