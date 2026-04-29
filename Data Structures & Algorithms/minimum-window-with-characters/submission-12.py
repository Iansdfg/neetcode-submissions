class Solution:
    def minWindow(self, s: str, t: str) -> str:

        res = ''
        min_len = len(s)
        slow=0
        s_freq = dict()
        t_freq = dict()

        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1

        for fast,char in enumerate(s):
            s_freq[char] = s_freq.get(char, 0) + 1

            while self.is_valid(s_freq, t_freq):
                if fast - slow + 1 <= min_len:
                    min_len = fast - slow + 1
                    res = s[slow:fast+1]
                s_freq[s[slow]] -= 1
                slow += 1 
        return res

    def is_valid(self, s_freq, t_freq):
        for char in t_freq.keys():
            if char not in s_freq:
                return False
            if s_freq[char] < t_freq[char]:
                return False
        return True 



        