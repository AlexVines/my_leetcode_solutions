def uniqueMorseRepresentations(words) -> int:
    """
    International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes,
    as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

    Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter.
    For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-...").
    We'll call such a concatenation, the transformation of a word.

    Return the number of different transformations among all words we have.

    >>> uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
    2
    """

    alpha = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
             "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    res = set()
    for word in words:
        morze = ''
        for letter in word:
            morze += alpha[ord(letter) - 97]
        res.add(morze)
    return len(res)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)