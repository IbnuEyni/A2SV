class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        m = len(set(nums))
        l = 0
        cnt = 0
        mapp = defaultdict(int)

        for r in range(n):
            mapp[nums[r]] += 1

            while len(mapp) == m:
                cnt += n - r
                mapp[nums[l]] -= 1
                if mapp[nums[l]] == 0:
                    del mapp[nums[l]]
                l += 1
        return cnt
