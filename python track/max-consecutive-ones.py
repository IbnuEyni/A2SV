class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_sum = 0
        sum_ = 0
        for num in nums:
           
            if num == 1:
                sum_ += 1
            else:
                max_sum = max(max_sum, sum_)
                sum_ = 0
        return max(max_sum, sum_)
