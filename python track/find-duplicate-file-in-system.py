class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        D = defaultdict(list)
        for path in paths:
            split_path = path.split()
            directory = split_path[0]
            files = split_path[1:]
            for file in files:
                filename, content = file.split('(')
                D[content].append(directory + '/' + filename)
        return [paths for paths in D.values() if len(paths) > 1]
