class Solution:
    def minWindow(self, s: str, t: str) -> str:

        res = ''
        min_len = len(s)
        slow=0
        s_freq = [0 for _ in range(52)]
        t_freq = [0 for _ in range(52)]

        for cha in t:
            if cha.islower():
                t_freq[ord(cha) - ord('a')]+=1
            else:
                t_freq[ord(cha) - ord('A') + 26] += 1


        for fast,char in enumerate(s):
            if char.islower():
                s_freq[ord(char) - ord('a')]+=1
            else:
                s_freq[ord(char) - ord('A') + 26] += 1

            while self.is_valid(s_freq, t_freq):
                if fast - slow + 1 <= min_len:
                    min_len = fast - slow + 1
                    res = s[slow:fast+1]

                if s[slow].islower():
                    s_freq[ord(s[slow]) - ord('a')] -= 1 
                else:
                    s_freq[ord(s[slow]) - ord('A') + 26] -= 1 

                slow += 1 

            
        return res

    def is_valid(self, s_freq, t_freq):
        for i in range(52):
            if s_freq[i] < t_freq[i]:
                return False
        return True 



        