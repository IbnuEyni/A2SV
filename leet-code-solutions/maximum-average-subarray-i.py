class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_ = sum(nums[:k])
        sum_ = max_
        for i in range(len(nums)-k):
            sum_ += nums[i+k] - nums[i] 
            max_ = max(max_, sum_) 
        return max_ / k