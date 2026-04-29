class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #key is target val, val is index
        val_index = dict()
        for index, val in enumerate(nums):
            if val in val_index:
                return [val_index[val], index]
            val_index[target - val] = index
        return 
            
