'''
876. 链表的中间结点

给你单链表的头结点 head ，请你找出并返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


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

    # 找到链表的中间节点
    middle = solution.middleNode(head)

    # 打印中间节点开始的链表
    print("\n中间节点开始的链表:")
    print_linked_list(middle)


if __name__ == "__main__":
    main()


