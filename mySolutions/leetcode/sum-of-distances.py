class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mapp = defaultdict(list)
        for i in range(len(nums)):    
            mapp[nums[i]].append(i)
        
        arr =  [0]*len(nums)
        for key, val in mapp.items():
            s = sum(val)
            pref = 0
            n = len(val)
            for i in range(n):
                pref = pref + val[i]
                arr[val[i]] = val[i]*(2*i-n+2) + s - 2*pref
        return arr


                
            
