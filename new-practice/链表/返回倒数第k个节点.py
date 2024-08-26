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
        flag = head
        num = 0
        while cur is not None:
            num += 1
            if num == k
            cur = cur.next






