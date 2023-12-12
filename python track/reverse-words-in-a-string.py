class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = s.split(" ")
        n = len(s) - 1
        res = []
        for i in range(n, -1, -1):
            if s[i].strip() != "":
                res.append(s[i])
        return " ".join(res)
