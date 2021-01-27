class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(tree):
    """
    Invert a binary tree.

    https://leetcode.com/problems/invert-binary-tree/

    """
    if tree is None:
        return None
    t_inv = TreeNode(tree.val)
    t_inv.left = invertTree(tree.right)
    t_inv.right = invertTree(tree.left)
    return t_inv
