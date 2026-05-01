from collections import deque 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        fast = 0 
        slow = 0
        res = []
        max_now = 0
        queue = deque([])

        for i in range(len(nums)):
            while queue and queue[0] <= i-k:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k-1: 
                # print(queue, nums[queue[0]])
                res.append(nums[queue[0]])
        return res


        

