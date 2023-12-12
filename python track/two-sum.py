class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx in range(len(nums)-1):
            for j in range(idx+1,  len(nums)):
                if nums[idx] + nums[j] == target:
                    return [idx, j]
            