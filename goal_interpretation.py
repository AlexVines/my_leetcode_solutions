def interpret(command):
    """
    Given an array of integers nums.

    A pair (i,j) is called good if nums[i] == nums[j] and i < j.

    Return the number of good pairs.

    >>> interpret("G()(al)")
    'Goal'
    >>> interpret("G()()()()(al)")
    'Gooooal'
    >>> interpret("(al)G(al)()()G")
    'alGalooG'

    """
    return command.replace('()', 'o').replace('(al)', 'al')


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)



