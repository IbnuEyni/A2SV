class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        stack = []
        temp = [0]*len(arr)
        res = 0

        for i in range(len(arr)):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            if stack:
                temp[i] = temp[stack[-1]] + arr[i]*(i-stack[-1])
            else:
                temp[i] = arr[i] * (i+1)

            stack.append(i)
            res += temp[i] 
            res %= ((10**9) + 7)
        return res