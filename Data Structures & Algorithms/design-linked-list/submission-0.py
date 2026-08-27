class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        while index > 0 and curr:
            index -= 1
            curr = curr.next
        
        if curr and curr != self.tail and index == 0:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        node, next, prev = Node(val), self.head.next, self.head
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtTail(self, val: int) -> None:
        node, next, prev = Node(val), self.tail, self.tail.prev
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev  

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        while index > 0 and curr:
            index -= 1
            curr = curr.next
        
        if curr and index == 0:
            node, next, prev = Node(val), curr, curr.prev
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev
        
    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        while index > 0 and curr:
            index -= 1
            curr = curr.next

        if curr and curr != self.tail and index == 0:
            next, prev = curr.next, curr.prev
            next.prev = prev
            prev.next = next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)