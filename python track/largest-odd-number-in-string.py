class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        n = len(num) - 1
        odd = {'1', '3', '5', '7', '9'}
        for i in range(n, -1, -1):
            if num[i] in odd:
                return num[:i+1]
        return ""

        