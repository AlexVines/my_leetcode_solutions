def maxDepth(root) -> int:
    """
    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest
    leaf node.

    https://leetcode.com/problems/maximum-depth-of-binary-tree/

    """
    if root is None:
        return 0

    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return max(left, right) + 1
