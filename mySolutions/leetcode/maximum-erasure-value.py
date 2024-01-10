class Solution(object):
    def maximumUniqueSubarray(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        frq = defaultdict(int)
        mx_sum = 0
        l = 0


        for r in range(len(arr)):

            frq[arr[r]] += 1

            while frq[arr[r]] > 1:
                frq[arr[l]] -= 1
                l += 1
            mx_sum  = max(mx_sum, sum(arr[l:r+1]))

        return mx_sum
