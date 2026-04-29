class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = self.getPrefix(nums)
        suffix = self.getPrefix(nums[::-1])[::-1]
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        return res


    def getPrefix(self, nums: List[int]) -> List[int]:
        prefix = []
        last = 1 
        for num in nums:
            prefix.append(last)
            last = last * num
        return prefix



