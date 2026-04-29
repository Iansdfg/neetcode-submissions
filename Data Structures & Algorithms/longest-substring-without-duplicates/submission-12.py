class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup = set()
        slow = 0
        max_len = 0
        for fast,char in enumerate(s):
            while char in dup:
                dup.remove(s[slow])
                slow += 1 
            dup.add(s[fast])
            max_len = max(max_len, fast - slow + 1)
        return max_len

