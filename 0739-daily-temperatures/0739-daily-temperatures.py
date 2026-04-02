class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []  # Stores indices of temperatures we are waiting to resolve
        
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                stack_i = stack.pop()
                res[stack_i] = i - stack_i
            stack.append(i)
        return res