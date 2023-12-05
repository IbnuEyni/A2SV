class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_ = max(candies)
        res = []
        for i in candies:
            res.append(i+extraCandies >= max_)
        return res