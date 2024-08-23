'''
206. 反转链表
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 常规list遍历串联：
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        headNew = newList
        cur = head
        l = list()
        while cur is not None:
            l.append(cur.val)
            cur = cur.next
        for i in range(len(l) - 1, -1, -1):
            newnode = ListNode(l[i])
            headNew.next = newnode
            headNew = newnode
        return newList.next


# 暴力指针：
class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        left = head
        right = head.next

        while right:
            tmp = right.next
            right.next = left
            while left.next != right:
                left = left.next
            left.next = tmp

            head = right

            right, left = left.next, right

        return head

def printList(head: Optional[ListNode]):
    """打印链表"""
    cur = head
    while cur:
        print(cur.val, end=" -> " if cur.next else "")
        cur = cur.next
    print()


def main():
    # 创建一个链表: 1 -> 2 -> 3 -> 4 -> 5
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head = ListNode(1, node2)

    # 打印原始链表
    print("原始链表:")
    printList(head)

    # 创建 Solution 实例并调用 reverseList 反转链表

    # 常规list遍历串联：
    solution = Solution()
    reversed_head = solution.reverseList(head)

    # 暴力指针：
    solution = Solution1()
    reversed_head1 = solution.reverseList(head)

    # 打印反转后的链表
    print("常规list遍历串联，反转后的链表:")
    printList(reversed_head)
    print("暴力指针，反转后的链表:")
    printList(reversed_head1)



# 运行主函数
if __name__ == "__main__":
    main()




