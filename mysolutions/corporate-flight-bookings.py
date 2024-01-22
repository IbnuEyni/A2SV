class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        res = [0] * (n+1)
        for book in bookings:
            res[book[0]-1] += book[2]

            res[book[1]] -= book[2]
        
        sum_ = 0
        for j in range(n):
            sum_ += res[j]
            res[j] = sum_

        return res[:n]


        