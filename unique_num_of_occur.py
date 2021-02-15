import collections
def uniqueOccurrences(arr) -> bool:
    """
    Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each
    value in the array is unique.
    >>> uniqueOccurrences([1,2,2,1,1,3])
    True
    >>> uniqueOccurrences([1, 2])
    False
    >>> uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
    True
    """
    counter = collections.Counter(arr)
    vals = []
    for i in counter:
        vals.append(counter[i])
    return len(set(vals)) == len(vals)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
