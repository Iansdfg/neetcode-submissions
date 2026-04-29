from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        res = 0
        max_count = 0
        char_cnt = defaultdict(int)
        for end, char in enumerate(s):
            char_cnt[char] += 1 
            max_count = max(max_count, char_cnt[char])

            while not self.isValid(s, k, start, end, max_count):
                char_cnt[s[start]] -= 1 
                start += 1 
            
            res = max(res, end - start + 1)
        return res 



    def isValid(self, s: str, k: int, start: int, end: int, max_count:int) -> bool:
        return end - start + 1 - max_count <= k 



        