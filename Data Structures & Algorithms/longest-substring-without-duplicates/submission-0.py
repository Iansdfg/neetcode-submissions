class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)

        left, right = 0, 1
        char_set = set([s[0]])
        max_len = 1

        while right < len(s):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1 

            max_len = max(max_len, right - left + 1)
            char_set.add(s[right])
            right += 1 



        return max_len