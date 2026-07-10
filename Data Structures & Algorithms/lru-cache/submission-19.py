class LinkedNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node = dict()
        self.head = LinkedNode(-1,-1)
        self.tail = LinkedNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.tail

    def get(self, key: int) -> int:
        if key in self.key_node:
            curr_node = self.key_node[key]
            self.remove(curr_node)
            self.add(curr_node)
            return curr_node.val
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.key_node:
            curr_node = self.key_node[key]
            curr_node.val = value
            self.remove(curr_node)
            self.add(curr_node)
        else:
            if len(self.key_node) >= self.capacity:
                self.remove(self.tail.prev)
            new_node = LinkedNode(key, value)
            self.add(new_node)

    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        del self.key_node[node.key]
        
    
    def add(self, node):
        next = self.head.next 

        node.next = next
        node.prev = self.head

        self.head.next = node 
        next.prev = node

        self.key_node[node.key] = node 
        

        
