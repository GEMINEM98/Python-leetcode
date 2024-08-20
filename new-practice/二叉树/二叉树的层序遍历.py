from collections import deque
from typing import List


# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 层序遍历函数：返回list
def levelOrderTraverse_list(root) -> List:
    if root is None:
        return

    res = []

    q = deque()
    q.append(root)
    while q:
        cur = q.popleft()
        res.append(cur.val)

        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
    return res


# 层序遍历函数：直接打印
def levelOrderTraverse_print(root) -> None:
    if root is None:
        return
    q = deque()
    q.append(root)
    while q:
        cur = q.popleft()
        # 访问 cur 节点
        print(cur.val)

        # 把 cur 的左右子节点加入队列
        if cur.left is not None:
            q.append(cur.left)
        if cur.right is not None:
            q.append(cur.right)

# 主函数
def main():
    # 构建一棵简单的二叉树
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    # 调用层序遍历函数
    print("层序遍历结果：")
    levelOrderTraverse_print(root)
    print(levelOrderTraverse_list(root))


# 运行主函数
if __name__ == "__main__":
    main()
