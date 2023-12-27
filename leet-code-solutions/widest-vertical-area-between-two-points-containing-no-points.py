class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        temp = []
        for i, j in points:
            temp.append(i)
        temp.sort()
        max_ = 0
        for i in range(1, len(temp)):
            dif = temp[i] - temp[i-1]
            max_ =  max(max_, dif)
        return max_
        