class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis = []
        can_use = ['(' for i in range(n)] + [')' for i in range(n)]
        visted = [0 for i in range(2*n)]
        self.dfs(can_use, visted, [], parenthesis)
        return parenthesis


    def dfs(self, can_use, visted, path, parenthesis):
        if len(path) == len(can_use) and self.is_valid(path):
            tar = ''.join(path[:])
            parenthesis.append(tar)
            return 

        for i in range(len(can_use)):
            if i > 0 and can_use[i] == can_use[i-1] and not visted[i-1]:
                continue
            if visted[i]:
                continue
            path.append(can_use[i])
            visted[i] = 1
            self.dfs(can_use, visted, path, parenthesis)
            visted[i] = 0
            path.pop()

    def is_valid(self, path):
        stack = []
        for char in path:
            if char == '(':
                stack.append('(')
            else:
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0 