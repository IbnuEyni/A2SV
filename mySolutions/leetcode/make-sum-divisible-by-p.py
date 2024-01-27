class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        tar = sum(nums) % p
        n = len(nums)
        if tar == 0:
            return 0

        mapp = {0:-1}
        rem = 0
        res = float('inf')

        for i, val in enumerate(nums):
            rem = (rem+val)%p

            if (rem-tar)%p in mapp:
                res = min(res, i - mapp[(rem-tar)%p])
         
            mapp[rem] = i
            
        return res if res < len(nums) else -1
        

    