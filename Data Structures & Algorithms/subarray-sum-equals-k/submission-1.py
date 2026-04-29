class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        sum_cnt = {0:1}
        res = 0
        for num in nums:
            curr_sum += num 
            if curr_sum - k in sum_cnt:
                res += sum_cnt[curr_sum - k]
           
            sum_cnt[curr_sum] = sum_cnt.get(curr_sum, 0) + 1
            
        print(sum_cnt)
        return res 

        
        