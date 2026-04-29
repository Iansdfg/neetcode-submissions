class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        visited = set()
        res = 0
        for num in num_set:
            if num in visited:
                continue
            increment = num + 1 
            length = 1
            while increment in num_set:
                visited.add(increment)
                increment += 1 
                length += 1 
            res = max(length, res)
        return res 


        