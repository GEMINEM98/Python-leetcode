'''
86. 分隔链表
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
你应当 保留 两个分区中每个节点的初始相对位置。
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        l = ListNode()
        left = l
        r = ListNode()
        right = r

        cur = head
        while cur:
            if cur.val < x:
                left.next = ListNode(cur.val)
                left = left.next
            else:
                right.next = ListNode(cur.val)
                right = right.next
            cur = cur.next

        print_linked_list(l.next)
        print_linked_list(r.next)

        left.next = r.next

        print_linked_list(l.next)

        return l.next

def print_linked_list(head1: ListNode):
    while head1:
        print(head1.val, end=" -> " if head1.next else "")
        head1 = head1.next
    print()

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node4 = ListNode(2)
    node5 = ListNode(5)
    node6 = ListNode(2)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    print("原始链表:")
    print_linked_list(node1)

    print(Solution().partition(head=node1, x=3))

