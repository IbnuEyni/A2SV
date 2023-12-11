class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """

        d = defaultdict()
        for i,j in reversed(operations):
            d[i] = d.get(j, j)
        for idn, val in enumerate(nums):
            if val in d:
                nums[idn] = d[val]
        return nums 