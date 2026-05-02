class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        sum_cun = {0:1}
        res = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum -k in sum_cun:
                res += sum_cun[prefix_sum -k]
            sum_cun[prefix_sum] = sum_cun.get(prefix_sum, 0)+1
        return res