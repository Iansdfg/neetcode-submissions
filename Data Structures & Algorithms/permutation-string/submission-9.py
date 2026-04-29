class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        slow = 0
        for fast in range(len(s1), len(s2)+1):
            if self.is_permutation(s2[slow: fast], s1):
                return True
            slow += 1 
            fast += 1 

        return False 

    # def include_permutation(self, s1, s2_char_freq):
    #     for char in s1:
    #         if not s2_char_freq[ord(char)-ord('a')]:
    #             return False 
    #     return True 

    def is_permutation(self, s1, s2):
        print(s1, s2)
        s1 = sorted(s1)
        s2 = sorted(s2)
        return s1 == s2