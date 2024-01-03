class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        opt = skill[0] + skill[-1]
        l = 0
        r = len(skill) - 1
        cnt = 0
        res = 0
        if len(skill) == 2:
            return skill[0] * skill[1]
        while l < r:
            if skill[l] + skill[r] == opt:
                cnt += 1
                res += skill[l]*skill[r]
                l += 1
                r -= 1
            elif skill[l] + skill[r] > opt:
                r -= 1
            else:
                l += 1
        if cnt < len(skill)//2:
            return -1
        else:
            return res
