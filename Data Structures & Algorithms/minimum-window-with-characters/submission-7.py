class Solution:
    def minWindow(self, s: str, t: str) -> str:

        res = ''
        min_len = len(s)
        slow=0
        s_freq = [0 for _ in range(52)]
        t_freq = [0 for _ in range(52)]

        for cha in t:
            t_freq[ord(cha) - ord('a')]+=1


        for fast,char in enumerate(s):
            s_freq[ord(char) - ord('a')] += 1 

            print(self.is_valid(s_freq,t_freq), fast, slow)
            while self.is_valid(s_freq, t_freq):
                if fast - slow + 1 <= min_len:
                    min_len = fast - slow + 1
                    res = s[slow:fast+1]
                    print(fast, slow, char, res)

                s_freq[ord(s[slow]) - ord('a')] -= 1 
                slow += 1 

            
        return res

    def is_valid(self, s_freq, t_freq):
        for i in range(52):
            if s_freq[i] < t_freq[i]:
                return False
        return True 



        