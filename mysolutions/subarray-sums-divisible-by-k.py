class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cur = 0
        counter = Counter()
        for num in nums:
            cur = (cur + num) % k
            counter[cur] += 1
        res = 0
        for e in counter:
            res += counter[e]*(counter[e]-1)//2
        return res + counter[0] 
        