class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        slow = 0
        max_len = 0
        for fast, char in enumerate(s):
            while s[fast] in visited:
                visited.remove(s[slow])
                slow += 1 
                
            max_len = max(max_len, fast - slow + 1)
            visited.add(s[fast])
        return max_len
        