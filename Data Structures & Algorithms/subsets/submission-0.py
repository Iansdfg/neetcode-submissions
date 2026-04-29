class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        subsets = []
        self.dfs(subset, subsets, 0, nums)
        return subsets


    def dfs(self, subset, subsets, index, nums):
        subsets.append(subset[:])
        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(subset, subsets,i+1, nums)
            subset.pop()
        