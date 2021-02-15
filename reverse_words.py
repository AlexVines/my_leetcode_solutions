def reverseWords(s: str) -> str:
    """
    Given a string, you need to reverse the order of characters in each word within a sentence while still preserving
    whitespace and initial word order.

    >>> reverseWords("Let's take LeetCode contest")
    "s'teL ekat edoCteeL tsetnoc"
    """
    words = ''
    for word in s.split():
        words += word[::-1] + ' '
    return words.rstrip()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
