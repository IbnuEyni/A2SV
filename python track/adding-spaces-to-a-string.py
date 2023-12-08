class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        res = []
        last_index = 0

        for i in spaces:
            res.append(s[last_index:i])
            last_index = i
        res.append(s[last_index:])

        return " ".join(res)
            
                