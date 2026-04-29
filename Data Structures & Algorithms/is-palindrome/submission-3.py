class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) -1 
        while left < right:
            while left < right and not self.isValid(s[left]):
                left += 1 
            while left < right and not self.isValid(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False

            left += 1 
            right -= 1
        return True
    
    def isValid(self, c: str)-> bool:
        return c.isalnum()
            

        