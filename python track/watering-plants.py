class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        pot = capacity
        step = 0
        for i, v in enumerate(plants):
            if capacity >= v:
                step += 1
                capacity -= v
            else:
                step += i+(i+1)
                capacity = pot-v
        return step