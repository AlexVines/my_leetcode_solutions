def maximum69Number(num) -> int:
    """
    Given a positive integer num consisting only of digits 6 and 9.

    Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

    >>> maximum69Number(9669)
    9969
    >>> maximum69Number(9996)
    9999
    >>> maximum69Number(9999)
    9999

    """
    return int(str(num).replace("6","9",1))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)