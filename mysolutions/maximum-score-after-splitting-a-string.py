class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """

        # sum_ = s.count('1', 1)
        # if s[0] == '0':
        #     sum_ += 1
        # ans = sum_
        # for c in s[1:len(s)-1]:
        #     if c == '0':
        #         sum_ += 1
        #     else:
        #         sum_ -= 1
        #     ans = max(ans, sum_)
        
        # return ans

        ones = s.count('1')
        mx = 0
        zeros  = 0

        for r in range(len(s)-1):
            if s[r] == '0':
                zeros += 1
            else:
                ones -= 1
            
            scr = ones + zeros
            mx = max(mx, scr)
        return mx