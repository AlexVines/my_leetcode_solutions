def removeOuterParentheses(S: str) -> str:
    """
    A valid parentheses string is either empty (""), "(" + A + ")", or A + B,
    where A and B are valid parentheses strings, and + represents string concatenation.
    For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

    A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into
    S = A+B, with A and B nonempty valid parentheses strings.

    Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are
    primitive valid parentheses strings.

    Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

    >>> removeOuterParentheses("(()())(())")
    '()()()'
    >>> removeOuterParentheses("(()())(())(()(()))")
    '()()()()(())'
    >>> removeOuterParentheses("()()")
    ''

    """
    opened = 0
    res = ''
    for letter in S:
        opened += 1 if letter == '(' else -1
        if opened == 1 and letter == '(':
            continue
        if opened == 0 and letter == ')':
            continue
        res += letter
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)