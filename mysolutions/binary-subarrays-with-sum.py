class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """ 
        cnt = 0
        l = 0
        sum_ = 0
        if goal < 0:
            return 0
        for r in range(len(nums)):
            sum_ += nums[r]
            while sum_ > goal:                
                sum_ -= nums[l]
                l += 1
            cnt += (r-l+1)
        
        if goal > 0:
            l = 0
            sum_ = 0
            for r in range(len(nums)):
                sum_ += nums[r]

                while sum_ > goal - 1:
                    sum_ -= nums[l]
                    l += 1

                cnt -= (r - l + 1)

        return cnt