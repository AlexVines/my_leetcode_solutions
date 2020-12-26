def kidsWithCandies(candies, extraCandies):
    """
    Given the array candies and the integer extraCandies, where candies[i] represents the number of candies
    that the ith kid has.

    For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the
    greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

    >>> kidsWithCandies([2,3,5,1,3], 3)
    [True, True, True, False, True]
    >>> kidsWithCandies([4,2,1,1,2], 1)
    [True, False, False, False, False]
    >>> kidsWithCandies([12,1,12], 10)
    [True, False, True]

    """
    max_ = max(candies)
    for i in range(len(candies)):
        candies[i] = candies[i] + extraCandies >= max_
    return candies


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)




