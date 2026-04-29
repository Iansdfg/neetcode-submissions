class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        res = 0
        char_set = set()
        for end, char in enumerate(s):
            while char in char_set:
                char_set.remove(s[start])
                start += 1 

            res = max(res, end - start + 1)

            char_set.add(char)

        return res 

        