def searchBST(self, tree, tofind: int):
    """
    You are given the root of a binary search tree (BST) and an integer val.

    Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
    If such a node does not exist, return null.

    """
    if tree.val == tofind:
        return tree
    if tree.val > tofind:
        if tree.left:
            return self.searchBST(tree.left, tofind)
    else:
        if tree.right:
            return self.searchBST(tree.right, tofind)
