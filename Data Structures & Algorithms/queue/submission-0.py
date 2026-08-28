class Node:
    def __init__(self, val, prev=None, next=None):
        self.val=val
        self.prev=prev
        self.next=next

class Deque:    
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        node, next, prev = Node(value), self.tail, self.tail.prev
        prev.next, next.prev = node, node
        node.next, node.prev = next, prev
        
    def appendleft(self, value: int) -> None:
        node, next, prev = Node(value), self.head.next, self.head
        prev.next, next.prev = node, node
        node.next, node.prev = next, prev
        
    def pop(self) -> int:
        if self.isEmpty():
            return -1
        prev, last, next = self.tail.prev.prev, self.tail.prev, self.tail
        prev.next, next.prev = next, prev

        return last.val
        
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        prev, first, next = self.head, self.head.next, self.head.next.next
        prev.next, next.prev = next, prev

        return first.val
