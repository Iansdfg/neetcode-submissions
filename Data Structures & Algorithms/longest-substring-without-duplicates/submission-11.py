class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        slow = 0
        max_len = 0
        for fast in range(len(s)):
            while s[fast] in visited:
                visited.remove(s[slow])
                slow += 1 

            visited.add(s[fast])
            max_len = max(max_len, fast - slow + 1)
        return max_len

        