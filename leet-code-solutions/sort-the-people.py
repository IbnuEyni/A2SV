class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        storage = {}
        i = 0
        while i < len(names):
            storage[heights[i]] = names[i]
            i +=1
        return [name for height,name in sorted(storage.items(), reverse=True)]
