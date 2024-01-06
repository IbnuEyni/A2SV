class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        l = r = 0
        res = []
        while l < len(firstList) and r < len(secondList):
            
            if firstList[l][0] >= secondList[r][0] and firstList[l][1] <= secondList[r][1]:
                if firstList[l][0] <= firstList[l][1]:
                    res.append([firstList[l][0], firstList[l][1]])
            elif firstList[l][0] < secondList[r][0] and firstList[l][1] <= secondList[r][1]:
                if secondList[r][0] <= firstList[l][1]:
                    res.append([secondList[r][0], firstList[l][1]])
            elif firstList[l][0] >= secondList[r][0] and firstList[l][1] > secondList[r][1]:
                if firstList[l][0] <= secondList[r][1]:
                    res.append([firstList[l][0], secondList[r][1]])
            elif firstList[l][0] < secondList[r][0] and firstList[l][1] > secondList[r][1]:
                if secondList[r][0] <= secondList[r][1]:
                    res.append([secondList[r][0], secondList[r][1]])
            if firstList[l][1] <= secondList[r][1]:
                l += 1
            else:
                r += 1
        return res
            
