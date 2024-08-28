
'''
判断链表是否包含环
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def huanNode(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False


def main():
    # 创建链表 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head


    # 创建 Solution 对象
    solution = Solution()

    print(solution.huanNode(head))



if __name__ == "__main__":
    main()




