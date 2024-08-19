
'''
707. 设计链表

你可以选择使用单链表或者双链表，设计并实现自己的链表。

单链表中的节点应该具备两个属性：val 和 next 。val 是当前节点的值，next 是指向下一个节点的指针/引用。

如果是双向链表，则还需要属性 prev 以指示链表中的上一个节点。假设链表中的所有节点下标从 0 开始。

实现 MyLinkedList 类：

MyLinkedList() 初始化 MyLinkedList 对象。
int get(int index) 获取链表中下标为 index 的节点的值。如果下标无效，则返回 -1 。
void addAtHead(int val) 将一个值为 val 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。
void addAtTail(int val) 将一个值为 val 的节点追加到链表中作为链表的最后一个元素。
void addAtIndex(int index, int val) 将一个值为 val 的节点插入到链表中下标为 index 的节点之前。如果 index 等于链表的长度，那么该节点会被追加到链表的末尾。如果 index 比长度更大，该节点将 不会插入 到链表中。
void deleteAtIndex(int index) 如果下标有效，则删除链表中下标为 index 的节点。

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()   # 定义一个空的头节点，后续节点往后面累加
        self.size = 0   # 维护一个链表的长度属性，方便后续写逻辑时使用

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:   # 处理边界条件
            return -1
        cur = self.head.next   # 空的头节点的下一个节点是真正意义上的用户定义节点
        for _ in range(index):   # 此时index已经符合下标的条件了
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:   # 处理下标越界情况
            return
        pre = self.head    # 前置节点指针指向空的头节点
        for _ in range(index):   # 遍历找到前置节点
            pre = pre.next
        pre.next = ListNode(val, pre.next)   # 新增节点的next指向目前前置节点的next，前置节点的next重新指向新增节点
        self.size += 1   # 新增节点需要更新链表的长度

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:   # 处理下标越界的情况
            return
        pre = self.head    # 前置节点指针指向空的头节点
        for _ in range(index):  # 遍历找到前置节点
            pre = pre.next
        pre.next = pre.next.next  # 前置节点的next指向后面节点的next的节点
        self.size -= 1   # 删除节点需要更新链表的长度

    def printList(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next


if __name__ == '__main__':
    # ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
    # [[], [1], [3], [1, 2], [1], [0], [0]]
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.printList()
    print("-----")
    obj.addAtTail(3)
    obj.printList()
    print("-----")
    obj.addAtIndex(1, 2)
    obj.printList()
    print("-----")
    obj.get(1)
    obj.printList()
    print("-----")
    obj.deleteAtIndex(1)
    obj.printList()
    print("-----")
    obj.get(1)
    obj.printList()
    print("-----")


# Your MyLinkedList object will be instantiated and called as such:
