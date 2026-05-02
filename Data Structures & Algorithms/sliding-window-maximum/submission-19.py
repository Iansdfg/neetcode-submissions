from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([])
        res = []
        for i in range(len(nums)):
            if queue and queue[0] <= i - k:
                queue.popleft()

            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            # print(i, nums[i], queue)

            if i-k+1 >= 0:
                res.append(nums[queue[0]])
        return res 


        