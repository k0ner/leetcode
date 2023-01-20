from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(2, numRows + 1):
            res.append([1] + [res[-1][j - 1] + res[-1][j] for j in range(1, i - 1)] + [1])
        return res


if __name__ == '__main__':
    print(Solution().generate(numRows=5))
    print(Solution().generate(numRows=1))
