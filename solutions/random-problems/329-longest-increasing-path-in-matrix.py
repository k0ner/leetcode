from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_r, max_c = len(matrix), len(matrix[0])
        rank = {}
        current_max = 1

        def dfs(r, c):
            if (r, c) not in rank:
                res = [0]
                current = matrix[r][c]
                if r + 1 < max_r:
                    if matrix[r + 1][c] > current:
                        res.append(dfs(r + 1, c))
                if r - 1 >= 0:
                    if matrix[r - 1][c] > current:
                        res.append(dfs(r - 1, c))
                if c + 1 < max_c:
                    if matrix[r][c + 1] > current:
                        res.append(dfs(r, c + 1))
                if c - 1 >= 0:
                    if matrix[r][c - 1] > current:
                        res.append(dfs(r, c - 1))
                rank[(r, c)] = 1 + max(res)
            return rank[(r, c)]

        for r in range(max_r):
            for c in range(max_c):
                current_max = max(current_max, dfs(r, c))

        return current_max


if __name__ == '__main__':
    print(Solution().longestIncreasingPath(matrix=[[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
    # print(Solution().longestIncreasingPath(matrix=[[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
    # print(Solution().longestIncreasingPath(matrix=[[1]]))
    # print(Solution().longestIncreasingPath())
