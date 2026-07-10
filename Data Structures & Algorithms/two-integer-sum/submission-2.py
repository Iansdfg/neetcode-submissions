class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remian_index = dict()
        for i,val in enumerate(nums):
            if val in remian_index:
                return [remian_index[val], i]
            remian_index[target - val] = i
        return[-1, -1]


        