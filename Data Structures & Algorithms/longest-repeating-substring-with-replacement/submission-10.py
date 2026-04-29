class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        slow, fast = 0, 0
        max_len = 0
        char_cnt = dict()
        max_frq = 0

        for fast in range(len(s)):
            char_cnt[s[fast]] = char_cnt.get(s[fast], 0) + 1
            max_frq = max(char_cnt[s[fast]], max_frq)

            while fast-slow+1 -  max_frq > k:
                char_cnt[s[slow]] = char_cnt.get(s[slow]) - 1
                if char_cnt[s[slow]] == 0:
                    del char_cnt[s[slow]] 
                slow += 1 

            max_len = max(max_len, fast-slow+1)

        return max_len



