class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        mapp = Counter(arr)
        for i in mapp:
            if mapp[i] > n/4:
                return i