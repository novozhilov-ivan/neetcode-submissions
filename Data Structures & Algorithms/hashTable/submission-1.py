class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
    
class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0

    def hash_function(self, val: int) -> int:
        return val % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        node = self.table[index]

        # если по индекс свободен для вставки
        if not node:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
        # если занят ищем некст индекс для вставки узла
            prev = None
            while node:
                if node.key == key:
                    node.value = value
                    return
                prev, node = node, node.next
            prev.next = Node(key, value)
            self.size += 1
        
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        node = self.table[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        node = self.table[index]

        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                self.size -= 1
                return True
            prev, node = node, node.next
        
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for node in self.table:
            while node:
                index = node.key % new_capacity
                if new_table[index] is None:
                    new_table[index] = Node(node.key, node.value)
                else:
                    new_node = new_table[index]
                    while new_node.next:
                        new_node = new_node.next
                    new_node.next = Node(node.key, node.value)
                node = node.next
        
        self.capacity = new_capacity
        self.table = new_table

