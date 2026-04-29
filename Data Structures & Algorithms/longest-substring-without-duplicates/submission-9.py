class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow, fast = 0, 0
        max_len = 0
        dup = set()
        while fast < len(s):
            while s[fast] in dup:
                dup.remove(s[slow])
                slow += 1 
            dup.add(s[fast])
            fast += 1 
            max_len = max(max_len, fast - slow)
        return max_len
