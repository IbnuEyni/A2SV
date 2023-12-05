class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        res = -1
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                res = max(res, int(num[i]))
        if res == -1:
            return ""
        else:
            return str(res) * 3
        