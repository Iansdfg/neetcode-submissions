class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        right_left = {
            ']':'[',
            ')':'(',
            '}':'{'
        }
        for char in s:
            if char in ['{','(','[']:
                stack.append(char)
            else:
                if not stack or stack.pop() != right_left[char]:
                    return False 
        return stack == []
