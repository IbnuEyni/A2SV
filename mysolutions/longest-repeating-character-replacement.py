class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        frq = defaultdict(int)
        frqt = 0
        mx_ln = 0
        l=0

        for r in range(len(s)):
            frq[s[r]] += 1
            frqt = max(frqt, frq[s[r]])
            while (r-l+1) - frqt > k:
                frq[s[l]] -= 1
                l += 1
            mx_ln = max(mx_ln, r-l+1)
        return mx_ln
        