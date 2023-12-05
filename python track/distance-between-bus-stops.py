class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """

        if start>destination:
            start,destination = destination,start
        sum1 = sum(distance)
        sum2 = sum(distance[start:destination])
        return min(sum1-sum2, sum2)