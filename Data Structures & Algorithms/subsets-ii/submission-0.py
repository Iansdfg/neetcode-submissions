class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset = []
        subsets = []
        self.dfs(nums, subset, subsets, 0)
        return subsets

    def dfs(self, nums, subset, subsets, level):
        subsets.append(subset[:])

        for i in range(level, len(nums)):
            if i > level and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            self.dfs(nums, subset, subsets, i+1)
            subset.pop()


        