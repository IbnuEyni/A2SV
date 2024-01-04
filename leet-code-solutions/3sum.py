class Solution:
    def threeSum(self, nums): 
        nums.sort()
        res=[]
        for i in range(len(nums)): 
            if i>0 and nums[i-1]==nums[i]: 
                continue 
			
			
            l=i+1 
            r=len(nums)-1  
            while l<r: 
                sum3=nums[i]+nums[l]+nums[r] 
                if sum3>0: 
                    r-=1  
                elif sum3<0: 
                    l+=1  
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1 
                    while nums[l]==nums[l-1] and l<r: 
                        l+=1   
        return res