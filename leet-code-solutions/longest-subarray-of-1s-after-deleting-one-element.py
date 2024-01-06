class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        cnt = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                cnt += 1
            
            while cnt > 1:
                if nums[l] == 0:
                    cnt -= 1
                l += 1
            res = max(res, r-l+1-cnt)

        if res == len(nums):
            return res - 1
        else:
            return res

        