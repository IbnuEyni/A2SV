class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        mx_ln = 0 
        seen = {}
        for r in range(len(s)):
            if seen.get(s[r], -1) >= l:
                l = seen[s[r]] + 1
            mx_ln = max(mx_ln, r-l+1)
            seen[s[r]] = r
        return mx_ln 
        