def heightChecker(heights) -> int:
    """
    Students are asked to stand in non-decreasing order of heights for an annual photo.

    Return the minimum number of students that must move in order for all students to be standing in non-decreasing
    order of height.

    Notice that when a group of students is selected they can reorder in any possible way between themselves and the
    non selected students remain on their seats.

    >>> heightChecker([1,1,4,2,1,3])
    3
    >>> heightChecker([5,1,2,3,4])
    5
    >>> heightChecker([1,2,3,4,5])
    0
    """
    result = sorted(heights)
    c = 0
    for i in range(len(heights)):
        if heights[i] != result[i]:
            c += 1
    return c


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
