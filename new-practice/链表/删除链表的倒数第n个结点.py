'''

---------------------------------------------------------------------------------------- leetcode没过

19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def kthToLast(self, head: ListNode, k: int) -> ListNode:
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
        return left

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newHead = ListNode()
        newHead.next = head
        node = self.kthToLast(head, n+1)
        node.next = node.next.next
        return newHead.next


def print_linked_list(head: Optional[ListNode]):
    """辅助函数：打印链表"""
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


def main():
    # 创建链表 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print("原始链表:")
    print_linked_list(head)

    # 创建 Solution 对象
    solution = Solution()

    # 设置 n 值，删除倒数第 n 个节点
    n = 2
    new_head = solution.removeNthFromEnd(head, n)

    print(f"\n删除倒数第 {n} 个节点后:")
    print_linked_list(new_head)


if __name__ == "__main__":
# ---------------------------------------------------------------------------------------- leetcode没过
    main()






