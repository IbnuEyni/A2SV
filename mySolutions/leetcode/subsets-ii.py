class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        path = []
        
        def subsetII(idx):
            if idx <= len(nums):
                # if path not in res:
                res.add(tuple(path))

            for i in range(idx, len(nums)):
                path.append(nums[i])
                subsetII(i+1)
                path.pop()
        subsetII(0)
        return list(res)