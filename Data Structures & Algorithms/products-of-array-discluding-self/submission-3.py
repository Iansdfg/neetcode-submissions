class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_p = [1 for i in range(len(nums))]
        right_p = [1 for i in range(len(nums))]
        res = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            left_p[i] = left_p[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            right_p[i] = right_p[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            res[i] = left_p[i] * right_p[i]

        return res

        