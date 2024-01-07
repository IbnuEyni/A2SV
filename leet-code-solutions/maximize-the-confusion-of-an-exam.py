class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        Tcnt = 0
        Fcnt = 0
        mx_cnt = 0
        l = 0
        for r in range(len(answerKey)):
            if answerKey[r] == 'T':
                Tcnt += 1
            else:
                Fcnt += 1

            while Tcnt > k  and Fcnt > k:
                if answerKey[l] == 'T':
                    Tcnt -= 1
                else:
                    Fcnt -= 1
                l += 1
            mx_cnt = max(mx_cnt, r-l+1)
        return mx_cnt
        
        