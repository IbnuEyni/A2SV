class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        indx = []
        word = []

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    indx.append(i+j)
                    word.append(list1[i])
        ans = min(indx)
        temp = []
        for k in range(len(indx)):
            if indx[k] == ans:
                temp.append(k)
        res = []
        for l in temp:
            res.append(word[l])
        return res



        