def freqAlphabets(s: str) -> str:
    """
    Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

    Characters ('a' to 'i') are represented by ('1' to '9') respectively.
    Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
    Return the string formed after mapping.

    It's guaranteed that a unique mapping will always exist.

    >>> freqAlphabets("10#11#12")
    'jkab'
    >>> freqAlphabets("1326#")
    'acz'
    >>> freqAlphabets("25#")
    'y'
    >>> freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#")
    'abcdefghijklmnopqrstuvwxyz'

    """
    for i in range(10, 27):
        s = s.replace(str(i) + '#', (chr(i + 96)))
    for j in range(10):
        s = s.replace(str(j), chr(j + 96))
    return s


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)