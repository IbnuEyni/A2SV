class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)-2):

            l=i+1
            r=len(nums) - 1
            while l<r:
                sum3 = nums[i] + nums[l] + nums[r]
                if abs(sum3-target) < abs(res-target):
                    res = sum3
                if sum3 < target:
                    l+=1
                elif sum3 > target:
                    r -=1
                else:
                    return res
        return res
