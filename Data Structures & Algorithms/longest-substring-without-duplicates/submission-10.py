class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow, fast = 0, 0
        max_len = 0
        dup = set()
        for fast in range(len(s)):
            while s[fast] in dup:
                dup.remove(s[slow])
                slow += 1 
            dup.add(s[fast])
            max_len = max(max_len, fast - slow + 1)
        return max_len
