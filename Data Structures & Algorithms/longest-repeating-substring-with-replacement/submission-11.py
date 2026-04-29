class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_cnt = dict()
        max_len = 0
        slow = 0
        for fast, char in enumerate(s):
            char_cnt[char] = char_cnt.get(char, 0) + 1

            # print(slow, fast, char_cnt, self.is_valid(slow, fast, char_cnt, k))
            while not self.is_valid(slow, fast, char_cnt, k):
                char_cnt[s[slow]] -= 1 
                if char_cnt[s[slow]] == 0:
                    del char_cnt[s[slow]]
                slow += 1 
            
            
            max_len = max(max_len, fast - slow + 1)
            
        return max_len

    def is_valid(self, slow, fast, char_cnt, k):
        return fast - slow + 1 - max(char_cnt.values()) <= k

        