def reverseString(s):
    """
    Write a function that reverses a string. The input string is given as an array of characters char[].

    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1)
    extra memory.

    You may assume all the characters consist of printable ascii characters.
    >>> reverseString(["h","e","l","l","o"])
    ['o', 'l', 'l', 'e', 'h']
    >>> reverseString(["H","a","n","n","a","h"])
    ['h', 'a', 'n', 'n', 'a', 'H']

    """

    def helper(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1)

    helper(0, len(s) - 1)
    return s


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)