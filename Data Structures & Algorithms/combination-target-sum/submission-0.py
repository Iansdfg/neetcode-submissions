class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        self.dfs(nums, target, 0, [], combinations)
        return combinations

    def dfs(self, nums: List[int], target: int, index, combination, combinations):
        
        if sum(combination) == target:
            combinations.append(combination[:])
            return 
            
        if sum(combination) > target:
            return 

        for i in range(index, len(nums)):
            combination.append(nums[i])
            self.dfs(nums, target, i, combination, combinations)
            combination.pop()


        