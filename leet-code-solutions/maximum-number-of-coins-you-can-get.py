class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        n = len(piles)
        sum_ = 0
        for i in range(n//3):
            sum_ += piles[((n-2)-(2*i))]
        return sum_
        