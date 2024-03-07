class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        self.cnt = 0
        def valid(n):
            if n < 1:
                return 0
            if n % 3 == 0:
                self.cnt += 1
            valid(n/3)
        valid(n)
        return pow(3, self.cnt) == n