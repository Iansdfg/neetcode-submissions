from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        res = 0 
        cha_cnt = defaultdict(int)
        for end, char in enumerate(s):
            cha_cnt[char] += 1 
            while not self.is_valid(start, end, max(cha_cnt.values()), k):
                cha_cnt[s[start]] -= 1 
                start += 1
            res = max(res, end - start + 1)
            
        return res 
    
    def is_valid(self, start, end, max_cnt, k):
        return end - start + 1 - max_cnt <= k 

        