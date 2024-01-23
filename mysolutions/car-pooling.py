class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        passSt = [0]*1001
        tot = 0

        for trp in trips:
            passSt[trp[1]] += trp[0]
            passSt[trp[2]] -= trp[0]

        for ps in passSt:
            tot += ps

            if tot > capacity:
                return False

        return True