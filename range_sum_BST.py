def rangeSumBST(self, root, low: int, high: int) -> int:
    """
    Given the root node of a binary search tree.
    Return the sum of values of all nodes with a value in the range [low, high].
    """
    if root is None:
        return 0
    elif root.val < low:
        return self.rangeSumBST(root.right, low, high)
    elif root.val > high:
        return self.rangeSumBST(root.left, low, high)
    return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)