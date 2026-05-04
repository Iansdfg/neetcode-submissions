from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([])
        res = []
        for index, num in enumerate(nums):

            if queue and index - k >= queue[0]:
                queue.popleft()
                
            while queue and num >= nums[queue[-1]]:
                queue.pop()

            queue.append(index)
            if index - k + 1 >= 0:
                res.append(nums[queue[0]])

        return res

        