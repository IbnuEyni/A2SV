class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        trans = []
        for i in ranges:
            
            for j in range(i[0], i[-1]+1):
                trans.append(j)

                
        for k in range(left, right+1):
            if k not in trans:
                return (False)
                break
        return True
    

        