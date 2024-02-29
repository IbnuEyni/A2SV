class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backtrack(idx):
            if len(path) == len(nums):
                res.append(path.copy())
                return 
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack(i+1)
                    path.pop()
            # for i in nums:
            #     path = [i]
            #     backtrack(path)

        backtrack(1)
        return res