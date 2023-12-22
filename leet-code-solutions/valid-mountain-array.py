class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        flg=0
        if(len(arr)==1):
            return False
        if(arr[1]<arr[0]):
            return False
        for i in range(1,len(arr)):
            if(flg==0 and arr[i]<arr[i-1]):
                flg=1
            if(flg==1 and arr[i]>arr[i-1] or arr[i]==arr[i-1]):
                return False
        return(flg==1)

        