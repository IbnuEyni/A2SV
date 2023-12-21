class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)-1
        num = 0
        for i in range(n, -1, -1):
            num += digits[i] * 10 ** abs(i-n)
        num += 1
        num =  str(num)
        res = []
        for i in num:
            res.append(int(i))
        return res

            