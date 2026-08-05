class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_i = dict()
        for i, num in enumerate(nums):
            if num in num_i:
                return [num_i[num], i]
            num_i[target - num] = i 
        return [-1, -1]
