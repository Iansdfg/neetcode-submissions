class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_len = 0
        slow = 0
        char_cnt = dict()
        for fast, char in enumerate(s):
            char_cnt[char] =  char_cnt.get(char, 0) + 1
            while not (fast - slow + 1 - max(char_cnt.values())<=k):
                char_cnt[s[slow]] -= 1  
                slow += 1  

            max_len = max(max_len, fast - slow + 1)
        return max_len
            

