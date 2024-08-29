'''
142. 环形链表 II

给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表。

'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:


    #  -----------------------------------------------------------------    set()解法
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()
        cur = head
        while cur is not None:
            s.add(cur)
            cur = cur.next
            if cur in s:
                return cur
        return None

        #  -----------------------------------------------------------------    快慢指针解法
    # def detectCycle2(self, head: Optional[ListNode]) -> Optional[ListNode]:



def main():
    # 创建链表：1 -> 2 -> 3 -> 4 -> 2 (形成一个循环)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # 形成环，node4 指向 node2

    solution = Solution()


    cycle_node = solution.detectCycle(node1)
    if cycle_node:
        print(f"Cycle detected at node with value: {cycle_node.val}")
    else:
        print("No cycle detected")


    cycle_node = solution.detectCycle2(node1)
    if cycle_node:
        print(f"Cycle detected at node with value: {cycle_node.val}")
    else:
        print("No cycle detected")


if __name__ == "__main__":
    main()





