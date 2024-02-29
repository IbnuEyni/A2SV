class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def combSum(idx):
            if target < 0:
                return 
            if target == 0:
                res.append(path.copy)
            if sum(path) == target:
                if path not in res:
                    res.append(path.copy())
            if sum(path) > target:
                return
            for i in range(idx, len(candidates)):
                path.append(candidates[i])
                combSum(i)
                combSum(i+1)
                path.pop()

        combSum(0)
        return res