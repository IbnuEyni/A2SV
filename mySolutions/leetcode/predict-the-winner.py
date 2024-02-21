class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        l = 0
        r = len(nums) - 1
        if not nums:
            return None
        def compare(l, r):
            if l > r:
                return 0
            
            return max((nums[l] -  compare(l+1, r)), (nums[r] - compare(l, r-1)))
        
        return compare(l, r) >= 0