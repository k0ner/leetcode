import collections
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        degree = collections.defaultdict(int)
        edges = collections.defaultdict(list)

        for pair in pairs:
            degree[pair[0]] += 1
            degree[pair[1]] -= 1
            edges[pair[0]].append(pair[1])

        # if we deal with eulerian circle start is the end :-)
        start = pairs[0][0]

        for v in degree:
            if degree[v] == 1:
                start = v

        res = []

        def dfs(from_):

            while edges[from_]:
                next = edges[from_].pop()
                dfs(next)

            res.append(from_)

        dfs(start)
        return [[res[i], res[i-1]] for i in range(len(res)-1, 0, -1)]


if __name__ == '__main__':
    print(Solution().validArrangement(pairs=[[5, 1], [4, 5], [11, 9], [9, 4]]))
    print(Solution().validArrangement(pairs=[[1, 3], [3, 2], [2, 1]]))
    print(Solution().validArrangement(pairs=[[1, 2], [1, 3], [2, 1]]))
    print(Solution().validArrangement(pairs=[[1, 2], [3, 2], [2, 1]]))
