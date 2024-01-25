class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        # temp1 = []
        # temp2 = []
        # cnt_0 = 0
        # cnt_1 = 0
        # for r in range(len(s)):
        #     if s[r] == '0':
        #         cnt_0 += 1
        #     else:
        #         cnt_1 += 1
        #     temp1.append(max(cnt_0, cnt_1))
        # cnt_0 = 0
        # cnt_1 = 0
        # for r in range(len(s)-1, -1, -1):
        #     if s[r] == '0':
        #         cnt_0 += 1
        #     else:
        #         cnt_1 += 1
        #     temp2.append(max(cnt_0, cnt_1))
        
        # mx= float('-inf')
        # for i in range(len(s)):
        #     sum_ = temp1[i] + temp2[::-1][i]
        #     mx = max(mx, sum_)
        # return mx

        sum_ = s.count('1', 1)
        if s[0] == '0':
            sum_ += 1
        ans = sum_
        for c in s[1:len(s)-1]:
            if c == '0':
                sum_ += 1
            else:
                sum_ -= 1
            ans = max(ans, sum_)
        
        return ans
