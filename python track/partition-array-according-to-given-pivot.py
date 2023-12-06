class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        les = []
        gret = []
        piv = []

        for i in nums:
            if i < pivot:
                les.append(i)
            elif i > pivot:
                gret.append(i)
            else:
                piv.append(i)
        return les+piv+gret
        