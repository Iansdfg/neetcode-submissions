class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        prefix_sum = 0 
        remainder_index = {0:-1}
        for index, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum%k 
            if remainder in remainder_index and index - remainder_index[remainder] >= 2:
                return True 
            if remainder not in remainder_index:
                remainder_index[remainder] = index 
        return False
                