class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = [] # temp, index

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIn = stack.pop()
                result[stackIn] = (i - stackIn)
            stack.append([t, i])
        
        return result