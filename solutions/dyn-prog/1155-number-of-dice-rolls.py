import math


class Solution:
    def numRollsToTarget(self, n: int, k: int, t: int) -> int:
        mod = (math.pow(10, 9) + 7)
        dp = [[0] * n for i in range(t + 1)]
        for i in range(1, min(t + 1, k + 1)):
            dp[i][0] = 1

        for i in range(1, n):
            for j in range(2, t + 1):
                if j > k:
                    sub = dp[j - k - 1][i - 1]
                else:
                    sub = 0
                dp[j][i] = int((dp[j - 1][i] + dp[j - 1][i - 1] - sub) % mod)

        return dp[t][n - 1]


if __name__ == '__main__':
    # print(Solution().numRollsToTarget(1, 6, 3))
    # print(Solution().numRollsToTarget(2, 6, 7))
    print(Solution().numRollsToTarget(30, 30, 500))
