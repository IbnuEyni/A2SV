class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
       

        def isDigit(n):
            res = 0
            while n > 0:
                digit = n % 10
                res += (digit * digit)
                n //= 10
            return res 

        seen = set()
        while n != 1:
            n = isDigit(n)
            if n in seen:
                return False
            seen.add(n)
        return True
