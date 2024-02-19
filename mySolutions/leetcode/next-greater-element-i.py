class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # if 
        stack = []
        res = [-1]*len(nums1)
        mapp = {}

        for i in range(len(nums1)):
            mapp[nums1[i]] = i
        for i in range(len(nums2)):
            num = nums2[i]
            while stack and stack[-1] < num:
                a = stack.pop()
                res[mapp[a]] = num
            if nums2[i] in mapp:
                stack.append(nums2[i])
        return res
