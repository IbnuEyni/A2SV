class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n, visited = len(nums), set()
        for i in range(n):
            if i not in visited:
                local_s = set()
                while True:
                    if i in local_s: return True
                    if i in visited: break          # credit to @crazyhyz, add this condition to avoid revisited
                    visited.add(i)
                    local_s.add(i)
                    prev, i = i, (i + nums[i]) % n
                    if prev == i or (nums[i] > 0) != (nums[prev] > 0): break
        return False