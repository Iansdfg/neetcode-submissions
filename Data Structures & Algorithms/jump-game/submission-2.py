class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farest = 0 
        for i in range(len(nums)):
            if i > farest:
                return False 

            farest = max(farest, i + nums[i])
        return farest >= len(nums) - 1
        