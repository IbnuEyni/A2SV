class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        cnt = Counter(s1)
        res = 0
        for i in range(len(s2)):
            if s2[i] in cnt:
                cnt[s2[i]] -= 1
                if cnt[s2[i]] == 0:
                    res += 1
            if i >= len(s1) and s2[i-len(s1)] in cnt:
                if cnt[s2[i-len(s1)]] == 0:
                    res -= 1
                cnt[s2[i-len(s1)]] += 1

            if res == len(cnt):
                return True 
        return False

        