def maxCoins(piles) -> int:
    """
    There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

    In each step, you will choose any 3 piles of coins (not necessarily consecutive).
    Of your choice, Alice will pick the pile with the maximum number of coins.
    You will pick the next pile with maximum number of coins.
    Your friend Bob will pick the last pile.
    Repeat until there are no more piles of coins.
    Given an array of integers piles where piles[i] is the number of coins in the ith pile.

    Return the maximum number of coins which you can have.

    >>> maxCoins([2,4,1,2,7,8])
    9
    >>> maxCoins([2,4,5])
    4
    >>> maxCoins([9,8,7,6,5,1,2,3,4])
    18
    """
    return sum(sorted(piles) [-2::-2][:len(piles)//3])


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)