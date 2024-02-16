class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        cnt = 0
        stack = []
        for i in s:
            if i == "(":
                stack.append(i)
                continue
            else:
                if not stack:
                    cnt += 1
                else:
                    if stack[-1] == "(":
                        stack.pop()
                continue
            cnt += 1
        return cnt + len(stack)