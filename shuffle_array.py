def shuffle(nums, n):
    """
    Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

    Return the array in the form [x1,y1,x2,y2,...,xn,yn].

    >>> shuffle([2,5,1,3,4,7], 3)
    [2, 3, 5, 4, 1, 7]
    >>> shuffle([1,2,3,4,4,3,2,1], 4)
    [1, 4, 2, 3, 3, 2, 4, 1]
    >>> shuffle([1,1,2,2], 2)
    [1, 2, 1, 2]

    """
    order = []
    for i in range(n):
        order.append(i)
        order.append(i + n)
    return [nums[i] for i in order]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)



