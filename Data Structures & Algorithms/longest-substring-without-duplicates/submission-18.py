class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        slow = 0
        max_len = 0
        for fast, char in enumerate(s):
            while char in char_set:
                char_set.remove(s[slow])
                slow += 1 
            char_set.add(char)
            max_len = max(max_len, fast - slow + 1)
        return max_len

        