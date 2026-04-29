class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = self.getPrefix(nums, False)
        suffix = self.getPrefix(nums, True)
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        return res


    def getPrefix(self, nums: List[int], reverse: bool) -> List[int]:
        prefix = []
        last = 1 
        if reverse:
            nums = list(reversed(nums))
        for num in nums:
            prefix.append(last)
            last = last * num

        if reverse:
            return list(reversed(prefix))
        return prefix



