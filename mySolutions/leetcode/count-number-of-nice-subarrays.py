class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        odd = 0
        l = 0
        sub_cnt = 0
        cnt = 0
        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                odd += 1
                sub_cnt = 0
                
            while odd == k:
                if nums[l] % 2:
                    odd -= 1
                sub_cnt += 1
                l += 1
            cnt += sub_cnt
        return cnt