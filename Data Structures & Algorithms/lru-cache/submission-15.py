class LinkedNode:
    def __init__(self, key:int, value: int, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.key2node = dict()
        self.capacity = capacity
        self.head = LinkedNode(-1, -1)
        self.tail = LinkedNode(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head
        

    def get(self, key: int) -> int:
        if key in self.key2node:
            res = self.key2node[key]
            self.remove(key, res)
            self.insert(key, res)
            return res.value
        else:
            return -1
        


    def put(self, key: int, value: int) -> None:
        if key in self.key2node:
            target = self.key2node[key]
            self.remove(key, self.key2node[key])
            new_node = LinkedNode(key, value)
            self.insert(key, new_node)
        else:
            if len(self.key2node) == self.capacity:
                target = self.tail.prev
                self.remove(target.key, target)
            new_node = LinkedNode(key, value)
            self.insert(key, new_node)


    def remove(self, key, node):
        prev = node.prev
        next = node.next
        prev.next, next.prev = next, prev

        node.next, node.prev = None, None
        del self.key2node[key]


    def insert(self, key, node):
        next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next
        next.prev = node
        self.key2node[key] = node
    
        