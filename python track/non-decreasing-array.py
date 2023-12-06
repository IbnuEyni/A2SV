class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = []

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                temp.append(i)
                if len(temp) > 1:
                    return False
                if i >= 2 and nums[i-2] > nums[i]:
                    nums[i] = nums[i-1]
        return True

      
        
            

        