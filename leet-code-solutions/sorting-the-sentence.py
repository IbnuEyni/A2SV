class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        spl = s.split()
        res = [""] * len(spl)

        for i in spl:
            idx = int(i[-1]) - 1
            res[idx] = i[:len(i)-1]
        return " ".join(res) 

