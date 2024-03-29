class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        stack = []
        nxtGreat = [0]*n
        
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                tmp = stack.pop()
                nxtGreat[tmp] = i - tmp
            stack.append(i)
        return nxtGreat