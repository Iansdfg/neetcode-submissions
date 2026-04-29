class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = [0 for i in range(26)]
        count = [0 for i in range(26)]

        for char in s1:
            need[ord(char)- ord('a')] += 1 
        
        slow = 0
        for fast, char in enumerate(s2):
            while fast - slow + 1 > len(s1):
                count[ord(s2[slow])- ord('a')] -= 1 
                slow += 1
            
            # if fast - slow + 1 == len(s1):
            count[ord(s2[fast]) - ord('a')] += 1
            if count == need:
                return True 

            print(slow, fast, s2[slow:fast+1]) 
        return False 