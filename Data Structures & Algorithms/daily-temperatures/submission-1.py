class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        mono_stack = []
        res = [0 for _ in range(len(temperatures))]
        for i, temperature in enumerate(temperatures):
            while mono_stack and temperatures[mono_stack[-1]]<temperature:
                target_index = mono_stack.pop()
                res[target_index] = i - target_index
            mono_stack.append(i)
        return res 

