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

        for i, val in enumerate(nums):
            rem = (rem+val)%p

            if (rem-tar)%p in mapp:
                if i - mapp[(rem-tar)%p] < n:
                    n = i-mapp[(rem-tar)%p]
            mapp[rem] = i
            
        return -1 if n == len(nums) else n
        

        