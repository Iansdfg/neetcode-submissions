class LinkedNode:
     def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None 
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node = dict()
        self.head = LinkedNode(-1, -1)
        self.tail = LinkedNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        """
        if node exist:
            get node
            remove node 
            insert node
            return node.val
        else:
            return -1
        """
        if key in self.key_node:
            node = self.key_node[key]
            self.remove(node)
            self.insert(node)
            return node.value
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        """
        if key not exist:
            if reach capacity:
                remove tail
            node = new node 
            insert node
        else:
            get node 
            change value 
            remove node
            insert node 
        """
        if key not in self.key_node:
            if len(self.key_node) >=  self.capacity:
                self.remove(self.tail.prev)
            node = LinkedNode(key, value)
            self.insert(node)
        else:
            node = self.key_node[key]
            node.value = value
            self.remove(node)
            self.insert(node)

    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        node.next = None
        node.prev = None
        
        del self.key_node[node.key]

    def insert(self,node):
        first = self.head.next

        self.head.next = node  
        node.prev = self.head

        node.next = first
        first.prev = node

        self.key_node[node.key] = node
        
