class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for slow in range(len(s)):
            fast = slow
            dup = set()
            while fast < len(s) and s[fast] not in dup:
                # print(dup, s[fast])
                dup.add(s[fast])
                fast += 1 
                max_len = max(max_len, fast - slow)
        return max_len
        