'''

// 二叉树的遍历框架
void traverse(TreeNode root) {
    if (root == null) {
        return;
    }
    // 前序位置
    traverse(root.left);
    // 中序位置
    traverse(root.right);
    // 后序位置
}

// N 叉树的遍历框架
void traverse(Node root) {
    if (root == null) {
        return;
    }
    // 前序位置
    for (Node child : root.children) {
        traverse(child);
    }
    // 后序位置
}

层序遍历：队列

'''

# 二叉树的前中后序遍历

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 前序遍历：
def preorder_traversal(root) -> list:
    if root is None:
        return []

    result = []

    # 访问根节点
    result.append(root.val)

    # 递归遍历左子树
    result.extend(preorder_traversal(root.left))

    # 递归遍历右子树
    result.extend(preorder_traversal(root.right))

    return result

# 中序遍历：
def inorder_traversal(root) -> list:
    if root is None:
        return []

    result = []

    # 递归遍历左子树
    result.extend(inorder_traversal(root.left))

    # 访问根节点
    result.append(root.val)

    # 递归遍历右子树
    result.extend(inorder_traversal(root.right))

    return result

# 后序遍历：
def postorder_traversal(root) -> list:
    if root is None:
        return []

    result = []

    # 递归遍历左子树
    result.extend(postorder_traversal(root.left))

    # 递归遍历右子树
    result.extend(postorder_traversal(root.right))

    # 访问根节点
    result.append(root.val)

    return result



if __name__ == '__main__':
    # 构造树节点
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # 前序遍历
    print("前序遍历:", preorder_traversal(root))  # 输出: [1, 2, 4, 5, 3]

    # 中序遍历
    print("中序遍历:", inorder_traversal(root))  # 输出: [4, 2, 5, 1, 3]

    # 后序遍历
    print("后序遍历:", postorder_traversal(root))  # 输出: [4, 5, 2, 3, 1]



