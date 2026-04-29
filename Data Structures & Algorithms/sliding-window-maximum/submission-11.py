from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([])
        res = []
        for i, num in enumerate(nums):

            while queue and num > nums[queue[-1]]:
                queue.pop()
            queue.append(i)

            if queue and queue[0] < i - k + 1:
                queue.popleft()

            if i+1 >= k:
                res.append(nums[queue[0]])
        
        return res 

        
            




        