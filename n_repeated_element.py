def repeatedNTimes(A):
    """
    In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

    Return the element repeated N times.

    >>> repeatedNTimes([1,2,3,3])
    3
    >>> repeatedNTimes([2,1,2,5,3,2])
    2
    >>> repeatedNTimes([5,1,5,2,5,3,5,4])
    5

    """
    count = {}
    for element in A:
        if element in count:
            count[element] += 1
            if count[element] == len(A) // 2:
                return element
        else:
            count[element] = 1


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)