class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count =  Counter(nums)
        multi_ele = []

        for ele, cnt in count.items():
            if cnt > len(nums)//3:
                multi_ele.append(ele)
        return multi_ele
        