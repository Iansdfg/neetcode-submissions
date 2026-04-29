class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        visited = [0 for _ in range(len(nums))]
        self.dfs(nums, 0, visited, [], subsets)
        return subsets


    def dfs(self, nums, index, visited, path, subsets):
        print(path)
        subsets.append(path[:])
        if index >= len(nums):
            return 
        for i in range(index, len(nums)):
            if visited[i] == 1:
                continue
            if i > index and nums[i] == nums[i-1]:
                continue

            path.append(nums[i])
            visited[i] = 1 
            self.dfs(nums, i + 1, visited, path, subsets)
            visited[i] = 0
            path.pop()
        