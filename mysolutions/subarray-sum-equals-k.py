class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k_sum = 0
        cnt = 0
        mapp = dict()
        mapp[0] = 1
        for r in range(len(nums)):
            k_sum += nums[r]
            cnt += mapp.get(k_sum-k, 0)
            mapp[k_sum] = mapp.get(k_sum, 0) + 1
        return cnt                