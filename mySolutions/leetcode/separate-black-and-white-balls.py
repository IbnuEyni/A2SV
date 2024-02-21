class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        l = 0
        temp = 0
        steps = 0
        for r in range(len(s)-1, -1, -1):
            if s[r] == '0':
                temp += 1
            else:
                steps += temp

        return steps
       