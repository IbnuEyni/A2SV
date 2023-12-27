class Solution(object):
    def numTimesAllBlue(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        ans = 0
        max_ = 0
        for i in range(len(flips)):            
            max_ = max(max_, flips[i])
            if max_ == i+1:
                ans += 1
        return ans
        