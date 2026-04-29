class LinkedNode:
    def __init__(self, key: int,  value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node = dict()
        self.head = LinkedNode(-1, -1)
        self.tail = LinkedNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1 
        target_node = self.key_node[key]
        self.remove(target_node)
        self.insert(target_node)
        return target_node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.key_node:
            if self.capacity == len(self.key_node):
                self.remove(self.tail.prev)          
            new_node = LinkedNode(key, value)
            self.insert(new_node)
        else:
            target_node = self.key_node[key]
            target_node.value = value
            self.remove(target_node)
            self.insert(target_node)

    def remove(self, node):
        prev = node.prev
        next = node.next 

        prev.next = next
        next.prev = prev

        node.next = None
        node.prev = None
        del self.key_node[node.key]


    def insert(self, node):
        self.key_node[node.key] = node
        firts = self.head.next

        self.head.next = node 
        firts.prev = node

        node.next = firts
        node.prev = self.head
        
