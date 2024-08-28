'''
面试题 02.02. 返回倒数第 k 个节点

实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        if head is None:
            return None

        cur = head
        left = head
        while cur:
            cur = cur.next
            if k == 0:
                left = left.next
            else:
                k -= 1

        if k != 0:
            return None
        return left.val


def main():
    # 创建链表 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # 创建 Solution 对象
    solution = Solution()

    # 设置 k 值，找倒数第 k 个节点的值
    k = 2
    result = solution.kthToLast(head, k)

    # 打印结果
    if result is not None:
        print(f"倒数第 {k} 个节点的值是: {result}")
    else:
        print(f"链表长度小于 {k}，无法找到倒数第 {k} 个节点")


if __name__ == "__main__":
    main()

