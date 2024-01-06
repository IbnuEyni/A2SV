class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0       
        res = 0
        cnt = 0
        vl = ['a', 'e', 'i', 'o', 'u']
        for i in range(k):
            if s[i] in vl:
                cnt += 1
        res = max(res, cnt)
        for r in range(k, len(s)):
            if s[r-k] in vl:
                cnt -= 1
            if s[r] in vl:
                cnt += 1
                res = max(res, cnt)
        return res
        