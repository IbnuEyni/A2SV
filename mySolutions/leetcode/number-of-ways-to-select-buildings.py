class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        N_0 = s.count('0')
        N_1 = len(s) - N_0

        pref_0 = pref_1 = cnt = 0
        for j in range(len(s)):
            if s[j] == '0':
                cnt += pref_1 * (N_1 - pref_1)
                pref_0 += 1
            else:
                cnt += pref_0 * (N_0 - pref_0)
                pref_1 += 1
        return cnt
            


