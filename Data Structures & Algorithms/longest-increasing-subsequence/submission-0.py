class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])

        return max(dp)
        