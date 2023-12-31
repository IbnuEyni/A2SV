class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        return sorted(points, key = lambda point: point[0] ** 2 + point[1] ** 2)[:k]
