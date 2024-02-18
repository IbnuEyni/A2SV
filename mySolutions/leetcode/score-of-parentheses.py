class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = [0]
        for i in s:
            if i == "(":
                stack.append(0)
            else:
                a = max(2 * stack.pop(), 1)
                stack[-1] += a
        
        return stack.pop()