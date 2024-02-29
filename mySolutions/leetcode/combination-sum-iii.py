class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []

        def combSumIII(idx, summ):
            if len(path) == k:
                if summ == n:
                    res.append(path.copy())
                    return
                return
            for i in range(idx, 10):
                path.append(i)
                combSumIII(i+1, summ+i)
                path.pop()
        combSumIII(1, 0)
        return res