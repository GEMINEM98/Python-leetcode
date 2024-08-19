
'''

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        head1 = list1
        head2 = list2
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next

        if head1 is not None:
            cur.next = head1
        if head2 is not None:
            cur.next = head2
        return head.next


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(8)))
    l2 = ListNode(1, ListNode(2, ListNode(6, ListNode(9))))
    l3 = Solution().mergeTwoLists(l1,l2)
    while l3:
        print(l3.val)
        l3 = l3.next





