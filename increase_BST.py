class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def increasingBST(root):
    """
    Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is
    now the root of the tree, and every node has no left child and only one right child.

    """
    def rebuild_tree(tr):
        elements = []
        if tr.left:
            elements += rebuild_tree(tr.left)

        # visit base node
        elements.append(tr.val)

        # visit right tree
        if tr.right:
            elements += rebuild_tree(tr.right)
        return elements

    ans = cur = TreeNode(None)
    elems = rebuild_tree(root)
    for v in elems:
        cur.right = TreeNode(v)
        cur = cur.right
    return ans.right