class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res = ""
        for j in range(len(s)):
            res += s[indices.index(j)]
        return res
