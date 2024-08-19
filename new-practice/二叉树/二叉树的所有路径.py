'''

二叉树的所有路径：

给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。

叶子节点 是指没有子节点的节点。

'''
import string
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#         res = []
#         path = ""
#         self.dfs(res, root, path)
#         return res
#
#     def dfs(self, res: list, root: Optional[TreeNode], path: string) -> None:
#         if not root:
#             return
#
#         path = path + str(root.val)
#
#         if root.left is None and root.right is None:
#             res.append(path)
#         else:
#             path = path + "->"
#             self.dfs(res, root.left, path)
#             self.dfs(res, root.right, path)


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        path = ""
        self.dfs(res, root, path)
        return res

    def dfs(self, res: list, root: Optional[TreeNode], path: string) -> None:
        if not root:
            return
        path += str(root.val)
        if root.left is None and root.right is None:
            res.append(path)
        else:
            self.dfs(res, root.left, path+"->")
            self.dfs(res, root.right, path+"->")


if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, right=TreeNode(5)), TreeNode(3))
    print(Solution().binaryTreePaths(root))


