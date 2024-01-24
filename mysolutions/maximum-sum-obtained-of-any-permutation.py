class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        M = 10**9+7
        n = len(nums)
        diff = [0]*(n+1)
        for start,end in requests:
            diff[start]+=1
            diff[end+1]-=1
        for i in range(1,n):
            diff[i]+=diff[i-1]
        nums.sort(reverse=True)
        diff=sorted(diff[:-1],reverse=True)
        result=0
        for i in range(n):
            result=(result%M+diff[i]*nums[i]%M)%M
        return result%M
        return int(ans%N)
        