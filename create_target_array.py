def createTargetArray(nums, index):
    """
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

-Initially target array is empty.
-From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
-Repeat the previous step until there are no elements to read in nums and index.

Return the target array.

It is guaranteed that the insertion operations will be valid.

    >>> createTargetArray([0,1,2,3,4], [0,1,2,2,1])
    [0, 4, 1, 3, 2]
    >>> createTargetArray([1,2,3,4,0], [0,1,2,3,0])
    [0, 1, 2, 3, 4]
    >>> createTargetArray([1], [0])
    [1]

    """
    lst = []
    for i in range(len(nums)):
        lst.insert(index[i], nums[i])
    return lst


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)


