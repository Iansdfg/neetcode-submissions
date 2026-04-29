class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutes = []
        visited = [0 for i in range(len(nums))]
        self.dfs(nums, visited, [], permutes)
        return permutes


    def dfs(self, nums, visited, path, permutes):
        if len(path) == len(nums):
            permutes.append(path[:])
            return

        for i in range(len(nums)):
            if visited[i]:
                continue

            path.append(nums[i])
            visited[i] = 1
            self.dfs(nums, visited, path, permutes)
            visited[i] = 0
            path.pop()





        