class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        n_set = set(nums)
        for i in nums:
            if (i-1) not in n_set:
                length = 1
                while (i+length) in n_set:
                    length += 1
                l = max(l, length)
        return l
        


        
        