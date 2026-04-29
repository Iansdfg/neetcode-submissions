class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_cnt = [0 for i in range(52)]
        t_cnt = [0 for i in range(52)]

        for char in t:
            t_cnt[ord(char) - ord('a')] += 1 
 
        slow = 0
        min_len = len(s)
        min_sub = ''
        for fast, char in enumerate(s):
            s_cnt[ord(char) - ord('a')] += 1 
            while slow <= fast and self.sub_valid(s_cnt, t_cnt):
                if fast - slow + 1 <= min_len:
                    min_sub = s[slow: fast + 1]
                    min_len = fast-slow+1

                s_cnt[ord(s[slow]) - ord('a')] -= 1 
                slow += 1
                
        return min_sub

    def sub_valid(self, s_cnt, t_cnt):
        for i in range(52):
            if t_cnt[i] > s_cnt[i]:
                return False 
        return True 
            
        