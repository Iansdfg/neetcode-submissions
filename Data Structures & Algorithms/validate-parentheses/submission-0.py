class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        right_left= {
            ')':'(' , 
            '}':'{' , 
            ']':'[' 
        }
        for char in s:
            if stack and char in [')', '}', ']'] and right_left[char] == stack[-1]:
                stack.pop()
                continue
            stack.append(char)
        return stack == []