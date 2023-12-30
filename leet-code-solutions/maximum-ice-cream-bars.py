class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        res = 0
        costs.sort()
        for i in range(len(costs)):
            if costs[i] <= coins:
                coins -= costs[i]
                res += 1
            else:
                break
        return res