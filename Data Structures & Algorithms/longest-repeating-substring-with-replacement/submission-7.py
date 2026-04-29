class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        slow, fast = 0, 0
        max_len = 0
        char_cnt = dict()
        while fast < len(s)+1:
            print(char_cnt)
            while not self.is_valid(char_cnt, fast-slow, k):
                char_cnt[s[slow]] = char_cnt.get(s[slow]) - 1
                if char_cnt[s[slow]] == 0:
                    del char_cnt[s[slow]] 
                slow += 1 

            if fast < len(s):
                char_cnt[s[fast]] = char_cnt.get(s[fast], 0) + 1  
            max_len = max(max_len, fast-slow)
            fast += 1

        return max_len


    def is_valid(self, char_cnt, length, k):
        print(length)
        most_char_cnt = 0
        for value in char_cnt.values():
            most_char_cnt = max(most_char_cnt, value)
        print(length - most_char_cnt <= k )
        return length - most_char_cnt <= k 



