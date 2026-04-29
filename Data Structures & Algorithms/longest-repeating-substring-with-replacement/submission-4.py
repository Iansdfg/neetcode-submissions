from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        res = 0
        end = 1
        while start < end:
            end = start + 1
            while end <= len(s) and self.isValid(s, k, start, end):
                end += 1
            res = max(res, end - start) 
            start += 1 
        return res - 1


    def isValid(self, s: str, k: int, start: int, end: int) -> int:
        cha_cnt = defaultdict(int)
        for char in s[start:end]:
            cha_cnt[char] += 1 
        if end - start - max(cha_cnt.values()) > k:
            return False 
        return True 



        