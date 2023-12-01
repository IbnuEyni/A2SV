class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        arr = []
        for i in words:
            arr.append([order.index(j) for j in i])
        return arr == sorted(arr)
        