class Solution:
    def myPow(self, x: float, n: int) -> float:
        return pow(x, n)
        if n == 0:
            return 0
        if n == 1:
            return 1

        if n < 0:
            return 1/self.myPow(x,-1*n)

        return x * self.myPow(x*x,n//2)