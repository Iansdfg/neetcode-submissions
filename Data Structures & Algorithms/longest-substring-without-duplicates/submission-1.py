class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)

        left, right = 0, 1
        char_cnt = dict()
        char_cnt[s[0]] = 1
        max_len = 1

        while right < len(s):
            char_cnt[s[right]] = char_cnt.get(s[right], 0) + 1 
            while not self.is_valid(char_cnt):
                if char_cnt[s[left]] > 0:
                    char_cnt[s[left]] -= 1 
                else:
                    del char_cnt[s[left]] 
                left += 1 

            max_len = max(max_len, right - left + 1)
            right += 1 

        return max_len

    def is_valid(self, char_cnt):
        return max(char_cnt.values()) <= 1 

