class Node:
    def __init__(self, val: int, nxt: "Node" | None = None):
        self.val = val
        self.nxt = nxt

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.nxt
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.nxt
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.nxt = self.head.nxt
        self.head.nxt = new_node
        if not new_node.nxt:
            self.tail = new_node 
        
    def insertTail(self, val: int) -> None:
        self.tail.nxt = Node(val)
        self.tail = self.tail.nxt
        
    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.nxt
        
        if curr and curr.nxt:
            if curr.nxt == self.tail:
                self.tail = curr
            curr.nxt = curr.nxt.nxt
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.nxt
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.nxt
        return res
        
