class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        lst = []
        for i in arr2:
            j = [i]*arr1.count(i)
            arr1.remove(i)
            lst.append(j)
            
        
        ans = sum(lst , [])
        temp = []
        
        for i in arr1:
            if i not in ans:
                temp.append(i)
                

        return ans + sorted(temp)