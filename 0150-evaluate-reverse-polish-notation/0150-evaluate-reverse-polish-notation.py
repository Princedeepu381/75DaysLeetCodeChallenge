class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                # Use int() for division to truncate toward zero, as required by the problem.
                # Standard Python floor division (//) truncates toward negative infinity.
                stack.append(int(b / a))
            else:
                stack.append(int(token))
                
        return stack[0]