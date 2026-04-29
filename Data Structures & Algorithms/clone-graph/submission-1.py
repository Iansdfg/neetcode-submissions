"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque 
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        queue = deque([node])
        old_new = dict()
        while queue:
            curr = queue.popleft()
            if curr not in old_new:
                old_new[curr] = Node(curr.val)
               
            for next_node in curr.neighbors:
                if next_node not in old_new:
                    queue.append(next_node)

                    new_next_node = Node(next_node.val)
                    old_new[next_node] = new_next_node
                old_new[curr].neighbors.append(old_new[next_node])

        return old_new[node]

                



        
        