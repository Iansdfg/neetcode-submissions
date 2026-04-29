class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        permutions = []
        visited = [0 for i in range(len(nums))]
        self.dfs(nums, visited, path, permutions)
        return permutions


    def dfs(self, nums, visited, path, permutions):
        if len(path) == len(nums):
            permutions.append(path[:])
        for i in range(len(nums)):
            if visited[i]:
                continue 
            path.append(nums[i])
            visited[i] = 1 
            self.dfs(nums, visited, path, permutions)
            visited[i] = 0 
            path.pop()

        