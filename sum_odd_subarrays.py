def sumOddLengthSubarrays(arr) -> int:
    """
    Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

    A subarray is a contiguous subsequence of the array.

    Return the sum of all odd-length subarrays of arr.

    >>> sumOddLengthSubarrays([1,4,2,5,3])
    58
    >>> sumOddLengthSubarrays([1,2])
    3
    >>> sumOddLengthSubarrays([10,11,12])
    66

    """
    length = len(arr)
    i = 1
    res = 0
    iter = length
    while i <= length:
        for j in range(iter):
            res += sum(arr[j:j + i])
        i += 2
        iter -= 2
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)