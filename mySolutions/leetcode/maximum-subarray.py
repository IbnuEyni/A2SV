class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summs = []
        summs.append(nums[0])
        mx_sum = nums[0]
        for i in range(1, len(nums)):
            summs.append(max((summs[i-1] + nums[i]), nums[i]))
            mx_sum = max(mx_sum, summs[i])
        return mx_sum 