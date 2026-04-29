class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        longest = 0
        slow = 0
        for fast, char in enumerate(s):
            while char in char_set:
                char_set.remove(s[slow])
                slow += 1 
            longest = max(fast - slow + 1, longest)
            char_set.add(char)

        return longest

        