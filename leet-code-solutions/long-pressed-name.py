class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = j  = 0 

        while i < len(name) and j < len(typed):
            if name[i] != typed[j]:
                return False
            l = r = 1
            while i+1 < len(name) and name[i] == name[i+1]:
                i += 1
                l += 1
            while j+1 < len(typed) and typed[j] == typed[j+1]:
                j += 1
                r += 1
            if r < l:
                return False
            i += 1
            j += 1
        return i == len(name) and j == len(typed)

            
            
        
        