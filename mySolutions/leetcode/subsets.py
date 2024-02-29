class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def subsets(idx):
            if idx <= len(nums):
                res.append(path.copy())
            
            for i in range(idx, len(nums)):
                path.append(nums[i])
                subsets(i+1)
                path.pop()
        subsets(0)
        return res
