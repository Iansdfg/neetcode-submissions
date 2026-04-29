class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        res = 0
        char_index = dict()
        for end, char in enumerate(s):
            if char in char_index:
                start = max(start, char_index[char] + 1)

            res = max(res, end - start + 1)

            char_index[char] = end

        return res 

        