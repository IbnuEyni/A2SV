class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            res.append(sum_)
        
        return res