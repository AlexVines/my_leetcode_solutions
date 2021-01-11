def busyStudent(startTime, endTime, queryTime: int) -> int:
    """
    Given two integer arrays startTime and endTime and given an integer queryTime.

    The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

    Return the number of students doing their homework at time queryTime. More formally,
    return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

    >>> busyStudent([1,2,3], [3,2,7], 4)
    1
    >>> busyStudent([4], [4], 4)
    1
    >>> busyStudent([4], [4], 5)
    0
    >>> busyStudent([1, 1, 1, 1], [1, 3, 2, 4], 7)
    0
    >>> busyStudent([9,8,7,6,5,4,3,2,1], [10,10,10,10,10,10,10,10,10], 5)
    5

    """
    res = 0
    for s, e in zip(startTime, endTime):
        if s <= queryTime and e >= queryTime:
            res += 1
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)