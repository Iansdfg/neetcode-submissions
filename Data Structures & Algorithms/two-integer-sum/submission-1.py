class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indx = dict()
        for index, num in enumerate(nums):
            if target - num in num_indx:
                return [min(index, num_indx[target - num]), max(index, num_indx[target - num])]
            num_indx[num] = index
        return []
            
        