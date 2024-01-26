class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # sum_ = sum(nums)
        # res = []
        # for i in range(len(nums)):
        #     # summ = 0
        #     # for j in range(len(nums)):
        #     #     summ += abs(nums[i]-nums[j])
        #     # res.append(summ)
        #     pre = sum(nums[:i])
        #     suf = sum(nums[i+1:])

        #     temp = (nums[i] * i - pre) + (suf - nums[i] * (len(nums)-i-1))
        #     res.append(temp)

        # return res

        sm,pr=sum(nums),0
        for i in range(len(nums)):
            pr+=nums[i]
            nums[i]=(((i+1)*nums[i]-pr)+(sm-pr)-(len(nums)-i-1)*nums[i])
        return nums