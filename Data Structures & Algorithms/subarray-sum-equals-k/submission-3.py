class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        sum_cnt = {0:1}
        res = 0
        for num in nums:
            prefix_sum = prefix_sum + num
            if prefix_sum - k in sum_cnt:
                res += sum_cnt[prefix_sum - k]
            sum_cnt[prefix_sum] = sum_cnt.get(prefix_sum, 0) + 1
        return res



        