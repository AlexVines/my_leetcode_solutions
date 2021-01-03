def numJewelsInStones(J: str, S: str) -> int:
    """
    You're given strings jewels representing the types of stones that are jewels,
    and stones representing the stones you have.

    Each character in stones is a type of stone you have.

    You want to know how many of the stones you have are also jewels.

    Letters are case sensitive, so "a" is considered a different type of stone from "A".
    >>> numJewelsInStones("aA", "aAAbbbb")
    3
    >>> numJewelsInStones("z","ZZ")
    0
    """
    jewels = set(J)
    count = 0
    for c in S:
        if c in jewels:
            count += 1
    return count


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
