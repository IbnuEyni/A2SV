class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        i = 0

        while i < len(s):
            if i < len(s)-2 and s[i+2] == "#":
                val = int(s[i:i+2])
                res.append(chr(val+96))
                i += 3
            else:
                res.append(chr(int(s[i]) + 96))
                i += 1

        return ''.join(res)

        