# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq 
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for index, node in enumerate(lists):
            heapq.heappush(heap, (node.val, index, node))
        dummy = ListNode(-1)
        curr = dummy

    
        while heap:
            top_val, index, top_node = heapq.heappop(heap)
            curr.next = top_node
            curr = top_node

            if top_node.next:
                heapq.heappush(heap, (top_node.next.val, index, top_node.next))
                top_node.next = None
        
        return dummy.next
        


        