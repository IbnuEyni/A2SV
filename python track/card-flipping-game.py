class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
     

        dict_same = {x for x, y in zip(fronts, backs) if x == y}
        return min([i for i in fronts + backs if i not in dict_same] or [0])
      
        
        