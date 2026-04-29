class ListNode:
    def __init__(self, key=None, val=None, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        # dummy-head-...-tail 
        # MRU-LRU
        self.key2node = dict()
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head 
        
    def put(self, key: int, value: int) -> None:
        # get target
        # move target node to head of linked list
        # if exceed, rm tail

        if key in self.key2node:
            target = self.key2node[key]
            self.remove(target)
            target.val = value
        else:
            target = ListNode(key, value)
            self.key2node[key] = target
        self.insert(target)


        if len(self.key2node) > self.capacity:
            old_last = self.tail.prev 
            del self.key2node[old_last.key]
            self.remove(old_last)
        

    def get(self, key: int) -> int:
        # get target
        # move target node to head of linked list

        if key not in self.key2node:
            return -1 

        target = self.key2node[key]
        self.remove(target)
        self.insert(target)

        return target.val 


    def insert(self, node:ListNode):
        old_first = self.head.next
        self.head.next = node
        node.next = old_first
        node.prev = self.head
        old_first.prev = node


    def remove(self, node:ListNode):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev
        








        
        
    
        
