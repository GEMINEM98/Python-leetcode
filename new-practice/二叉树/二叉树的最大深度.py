
'''
104. 二叉树的最大深度

给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = 0
        self.depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.traverse(root)
        return self.res

    def traverse(self, root: TreeNode) -> None:
        if root is None:
            return

        self.depth += 1
        if root.left is None and root.right is None:
            self.res = max(self.depth, self.res)
        else:
            self.traverse(root.left)
            self.traverse(root.right)
        self.depth -= 1








