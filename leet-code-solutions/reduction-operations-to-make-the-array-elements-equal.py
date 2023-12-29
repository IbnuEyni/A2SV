class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse =  True)
        res = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                res += i+1
        return res