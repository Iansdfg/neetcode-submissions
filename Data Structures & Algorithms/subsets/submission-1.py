class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self.backtrack(nums, 0, [], subsets)
        return subsets

    def backtrack(self, nums: List[int], index, subset, subsets):
        subsets.append(subset[:])

        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.backtrack(nums, i+1, subset, subsets)
            subset.pop()

            

            
        