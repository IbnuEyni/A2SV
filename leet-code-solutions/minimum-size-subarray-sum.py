class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        sum_ = 0
        mn_ln = float('inf') 
        for r in range(len(nums)):
            sum_ += nums[r]
            while sum_ >= target:
                mn_ln = min(mn_ln, r-l+1)
                sum_ -= nums[l]
                l += 1

        if mn_ln < float('inf'):
            return mn_ln
        else:
            return 0