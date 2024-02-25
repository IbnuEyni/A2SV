class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        limit = cnt = 0
        for i in range(len(nums)):
            if nums[i] > limit + 1:
                while nums[i] > limit+1:
                    limit += limit+1
                    cnt += 1
                    if limit >= n:
                        break
            limit += nums[i]
            if limit >= n:
                break
        while limit < n:
            limit += limit+1
            cnt += 1
        return cnt