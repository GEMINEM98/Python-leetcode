'''
160. 相交链表

给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

图示两个链表在节点 c1 开始相交：

题目数据 保证 整个链式结构中不存在环。

注意，函数返回结果后，链表必须 保持其原始结构 。

自定义评测：

评测系统 的输入如下（你设计的程序 不适用 此输入）：

intersectVal - 相交的起始节点的值。如果不存在相交节点，这一值为 0
listA - 第一个链表
listB - 第二个链表
skipA - 在 listA 中（从头节点开始）跳到交叉节点的节点数
skipB - 在 listB 中（从头节点开始）跳到交叉节点的节点数
评测系统将根据这些输入创建链式数据结构，并将两个头节点 headA 和 headB 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被 视作正确答案 。

'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 链表加和遍历：
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA = headA
        curB = headB
        while curA != curB:
            if curA:
                curA = curA.next
            else:
                curA = headB
            if curB:
                curB = curB.next
            else:
                curB = headA
        return curA


# set判断：
class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA = headA
        curB = headB
        setA = set()
        while curA:
            setA.add(curA)
            curA = curA.next
        while curB:
            if curB in setA:
                return curB
            else:
                curB = curB.next
        return


def main():
    # 构建两个链表：
    # 链表 A: 4 -> 1 -> 8 -> 4 -> 5
    # 链表 B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
    # 交点在值为 8 的节点处
    common = ListNode(8)
    common.next = ListNode(4)
    common.next.next = ListNode(5)

    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = common

    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = common

    # 创建 Solution 实例并调用 getIntersectionNode

    # 链表加和遍历：
    solution = Solution()
    intersection = solution.getIntersectionNode(headA, headB)

    if intersection:
        print(f"两个链表相交于节点值为: {intersection.val}")
    else:
        print("两个链表不相交")

    # set判断：
    solution = Solution1()
    intersection = solution.getIntersectionNode(headA, headB)

    if intersection:
        print(f"两个链表相交于节点值为: {intersection.val}")
    else:
        print("两个链表不相交")


# 运行主函数
if __name__ == "__main__":
    main()
