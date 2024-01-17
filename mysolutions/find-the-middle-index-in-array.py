class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l_sum = 0
        r_sum = 0
        t_sum = sum(nums)
        res = -1
        for i in range(len(nums)):
            l_sum = sum(nums[:i])
            r_sum = t_sum - l_sum - nums[i]
            if l_sum == r_sum:
                res = i 
                break
        return res