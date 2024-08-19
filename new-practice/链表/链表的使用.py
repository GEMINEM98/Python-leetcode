'''

链表的使用

给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字0之外，这两个数都不会以0开头。

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

'''

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        current = res

        carry = 0

        while l1 or l2 or carry:
            if l1:
                l1val = l1.val
            else:
                l1val = 0
            if l2:
                l2val = l2.val
            else:
                l2val = 0

            sum = l1val + l2val + carry
            current.next = ListNode(sum % 10)
            carry = sum // 10

            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return res.next


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    res = Solution().addTwoNumbers(l1, l2)
    while res:
        print(res.val)
        res = res.next
