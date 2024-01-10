class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        min_count = float('inf')
        for i in range(len(blocks)):
            black_count, white_count = 0, 0
            for j in range(i, len(blocks)):
                if blocks[j] == 'B':
                    black_count += 1
                else:
                    white_count += 1
                if black_count + white_count == k:
                    min_count = min(min_count, white_count)
                    break
        return min_count
        