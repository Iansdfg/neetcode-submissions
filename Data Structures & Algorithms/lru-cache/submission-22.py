class linkedNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None 
        self.prev = None 


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node = dict()
        self.head = linkedNode(-1, -1)
        self.tail = linkedNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.key_node:
            node = self.key_node[key]
            self.remove(node)
            self.add(node)
            return node.value
        else:
            return -1 
    
    def put(self, key: int, value: int) -> None:
        if key in self.key_node:
            node = self.key_node[key]
            node.value = value
            self.remove(node)
            self.add(node)
        else:
            if len(self.key_node) == self.capacity:
                self.remove(self.tail.prev)
            new_node = linkedNode(key, value)
            self.add(new_node)

    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        node.next = None
        node.prev = None

        del self.key_node[node.key]


    def add(self, node):
        first = self.head.next 

        self.head.next = node
        first.prev = node

        node.next = first
        node.prev = self.head

        self.key_node[node.key] = node
        
