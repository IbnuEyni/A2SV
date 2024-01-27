class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum_ = sum(nums)
        pre = 0
        res = []
        for i in range(len(nums)):
            # summ = 0
            # for j in range(len(nums)):
            #     summ += abs(nums[i]-nums[j])
            # res.append(summ)
            pre += nums[i]
            suf = sum_ - pre

            temp = (nums[i] * i - (pre-nums[i])) + (suf - nums[i] * (len(nums)-i-1))
            res.append(temp)

        return res
