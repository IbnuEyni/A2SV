class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = []
        neg = []

        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)
        res = []
        for i in range(len(nums)//2):
            res.append(pos[i])
            res.append(neg[i])
        return res