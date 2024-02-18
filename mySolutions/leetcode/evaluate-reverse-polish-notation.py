class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        oper = ['+', '-', '*', '/']

        for i in range(len(tokens)):
            if tokens[i] not in oper:
                stack.append(int(tokens[i]))
            else:
                if stack:
                    a = stack.pop()
                    b = stack.pop()
                    if tokens[i] == '+':
                        stack.append(a + b)
                    elif tokens[i] == '-':
                        stack.append(b - a)
                    elif tokens[i] == '*':
                        stack.append(a * b)
                    else:
                        stack.append(int(b / a))
        return stack[-1]