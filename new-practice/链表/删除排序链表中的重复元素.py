'''
83. 删除排序链表中的重复元素

给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        left = head
        right = head.next
        while right:
            if right.val != left.val:
                left = left.next
                left.val = right.val
                left.next = right.next
            right = right.next
        left.next = None
        return head


def print_linked_list(head: Optional[ListNode]) -> None:
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next


def main():
    # 创建链表：1 -> 1 -> 2 -> 3 -> 3
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(3)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print("Original linked list:")
    print_linked_list(node1)

    # 删除重复元素
    solution = Solution()
    result_head = solution.deleteDuplicates(node1)

    print("Linked list after removing duplicates:")
    print_linked_list(result_head)


if __name__ == "__main__":
    main()


