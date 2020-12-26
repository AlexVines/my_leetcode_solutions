def defangIPaddr(address: str) -> str:
    """
    Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

    Return the array in the form [x1,y1,x2,y2,...,xn,yn].

    >>> defangIPaddr("1.1.1.1")
    '1[.]1[.]1[.]1'
    >>> defangIPaddr("255.100.50.0")
    '255[.]100[.]50[.]0'
    """
    return address.replace('.', '[.]')


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)