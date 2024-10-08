'''
23. 合并 K 个升序链表

给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。
'''
import heapq
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




'''
最小堆：：
最小堆的根节点永远是最小的
'''

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return None
        min_heap = []

        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))

        head = ListNode(0)
        cur = head
        while min_heap:
            # 获取最小节点，接到结果链表中
            smallest, index, node = heapq.heappop(min_heap)
            cur.next = ListNode(smallest, None)
            cur = cur.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, index, node.next))
        return head.next




'''
暴力解：
两两进行合并，直到合并完最后一个链表即可
'''

class Solution1:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return None

        j = 1
        i = lists[0]
        while j < len(lists):
            p = Solution1().mergeTwoLists(i, lists[j])
            i = p
            j += 1
        return i

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


def main():
    # 创建测试用的链表
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))

    # 将链表放入列表
    lists = [list1, list2, list3]



    # 最小堆解法：
    solution = Solution()
    merged_list = solution.mergeKLists(lists)

    # 输出合并后的链表
    current = merged_list
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")  # 表示链表结束


    # 暴力解法：两两相排
    solution1 = Solution1()
    merged_list1 = solution1.mergeKLists(lists)

    # 输出合并后的链表
    current = merged_list1
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")  # 表示链表结束


if __name__ == "__main__":
    main()



