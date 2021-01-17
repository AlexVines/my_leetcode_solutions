def selfDividingNumbers(left: int, right: int):
    """
    A self-dividing number is a number that is divisible by every digit it contains.

    For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

    Also, a self-dividing number is not allowed to contain the digit zero.

    Given a lower and upper number bound, output a list of every possible self dividing number,
    including the bounds if possible.

    >>> selfDividingNumbers(1, 22)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

    """

    def is_selfdiv(num):
        n = str(num)
        for ch in n:
            if ch == '0' or num % int(ch) > 0:
                return False
        return True

    return [i for i in range(left, right + 1) if is_selfdiv(i)]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)