class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for token in tokens:
            print(token, stack)
            if token == "+":
                first = int(stack.pop())
                second = int(stack.pop())
                stack.append(str(first + second))
            elif token == "-":
                first = int(stack.pop())
                second = int(stack.pop())
                stack.append(str(second - first))
            elif token == "*":
                first = int(stack.pop())
                second = int(stack.pop())
                stack.append(str(first * second))
            elif token == "/":
                first = int(stack.pop())
                second = int(stack.pop())
                stack.append(str(int(second / first)))
            else:
                stack.append(token)
            
        return int(stack[-1])

        