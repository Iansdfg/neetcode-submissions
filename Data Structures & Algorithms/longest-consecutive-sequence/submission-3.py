class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums:
            curr = num - 1
            max_consecutive = 1
            while curr in nums_set:
                max_consecutive +=1
                curr -= 1 
            res = max(max_consecutive, res)
        return res


        