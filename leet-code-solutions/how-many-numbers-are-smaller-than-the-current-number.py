class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num = sorted(nums)
        res = []
        for i in nums:
           res.append(num.index(i))
        return res